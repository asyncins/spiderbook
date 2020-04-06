import requests
import parsel
from urllib.parse import urljoin
from common import channel, queue


urls = ["https://www.phei.com.cn/xwxx/index_{}.shtml".format(i) for i in range(1, 46)]
urls.append("https://www.phei.com.cn/xwxx/index.shtml")

for url in urls:
    # 翻页爬取
    resp = requests.get(url)
    sel = parsel.Selector(resp.content.decode("utf8"))
    li = sel.css(".web_news_list ul li.li_b60")
    for news in li:
        link = news.css("a:first-child::attr('href')").extract_first()
        full_link = urljoin(url, link)  # 拼接完整 URL
        # 将新闻资讯详情页 URL 发布到 RabbitMQ 队列
        channel.queue_declare(queue=queue)
        channel.basic_publish(exchange='',
                              routing_key=queue,
                              body='{}'.format(full_link))
        print("[x] Sent '{}'".format(urljoin(url, link)))