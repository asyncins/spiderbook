import parsel


sel = parsel.Selector(html)
publisher = sel.xpath("//span[@class='publisher']/text()").extract_first()
pub_time = sel.xpath("//span[@class='pubTime']/text()").extract_first()
content = "\n".join(sel.xpath("//div[@class='content']/p/text()").extract())

print(publisher, "\n", pub_time, "\n", content)