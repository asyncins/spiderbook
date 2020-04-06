import re
import parsel
import requests


url = "https://www.phei.com.cn/gywm/cbsjj/2010-11-19/47.shtml"
req = requests.get(url)
text = req.content.decode("utf8")
title = re.search("<h1>(.*)</h1>", text).group(1)
sel = parsel.Selector(text)
content = "\n".join(sel.css(".column_content_inner p font::text").extract())
with open("about.txt", "a") as file:
    file.write(title)
    file.write("\n")
    file.write(content)