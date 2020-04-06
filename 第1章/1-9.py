import requests
import parsel
from urllib.parse import urljoin
from pymongo import MongoClient

# 连接数据库并指定数据库和集合
client = MongoClient('localhost', 27017)
db = client.news
collection = db.phei


urls = ["https://www.phei.com.cn/xwxx/index_{}.shtml".format(i) for i in range(45)]
urls.append("https://www.phei.com.cn/xwxx/index.shtml")

for url in urls:
    # 翻页爬取
    resp = requests.get(url)
    sel = parsel.Selector(resp.content.decode("utf8"))
    li = sel.css(".web_news_list ul li.li_b60")
    for news in li:
        # 从单页中提取资讯信息
        title = news.css("p.li_news_title::text").extract_first()
        pub_time = news.css("span::text").extract_first()
        desc = news.css("p.li_news_summary::text").extract_first()
        image = news.css("div.li_news_line img::attr('src')").extract_first()
        full_image = urljoin(url, image)  # 完整图片链接
        # 将数据存入 MongoDB 数据库中
        collection.insert_one({"title": title, "pubTime": pub_time,
                               "image": full_image, "desc": desc})