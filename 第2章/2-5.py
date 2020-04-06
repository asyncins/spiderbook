import asyncio
import re
from pyppeteer import launch

async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('https://www.phei.com.cn/module/goods/wssd_index.jsp')
    lis = await page.querySelectorAll("#book_sort_area ul:nth-child(1) li")
    for i in lis:
        image_element = await i.querySelector("p a img")
        image = await (await image_element.getProperty("src")).jsonValue()
        book_element = await i.querySelector("p.li_title  a")
        book = await (await book_element.getProperty("textContent")).jsonValue()
        author_price_element = await i.querySelector("p.li_author")
        author_price = await (await author_price_element.getProperty("textContent")).jsonValue()
        try:
            author = re.search("作译者：(.*)定价", str(author_price)).group(1)
            price = re.search(r"(\d+.\d+)", str(author_price)).group(1)
        except Exception as exc:
            author, price = "", ""
            print(exc)
        print([book, price, author, image])
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())