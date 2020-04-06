import re
import requests
import parsel
from urllib.parse import urljoin
from common import channel, queue
from common import detail


def callback(ch, method, properties, body):
    url = str(body, "utf8")
    print(url)
    resp = requests.get(url)
    sel = parsel.Selector(resp.content.decode("utf8"))
    the_time = sel.css(".news_date::text").extract_first()
    pub_time = re.search("(\d+-\d+-\d+)", the_time).group(1)
    # 为保持文章排版和样式，保留标签
    contents = sel.css(".news_content p").extract()
    content = "\n".join(contents)
    # 将文章数据存入 MongoDB
    detail.insert_one({"pubTime": pub_time, "url": url, "content": content})


channel.basic_consume(
    queue=queue, on_message_callback=callback, auto_ack=True)

channel.start_consuming()