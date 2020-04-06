import parsel


sel = parsel.Selector(html)
publisher = sel.css(".publisher::text").extract_first()
pub_time = sel.css(".pubTime::text").extract_first()
content = "\n".join(sel.css(".content p::text").extract())

print(publisher, "\n", pub_time, "\n", content)