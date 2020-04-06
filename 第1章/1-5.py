import re
import aiohttp
import asyncio
import parsel


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, 'https://www.phei.com.cn/gywm/cbsjj/2010-11-19/47.shtml')
        title = re.search("<h1>(.*)</h1>", html).group(1)
        sel = parsel.Selector(html)
        content = "\n".join(sel.css(".column_content_inner p font::text").extract())
        with open("about.txt", "a") as file:
            file.write(title)
            file.write("\n")
            file.write(content)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())