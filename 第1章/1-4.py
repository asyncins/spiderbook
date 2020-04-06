from datetime import datetime
import asyncio


async def wait():
    asyncio.sleep(5)
    print("等我 5 秒钟")


async def print_time(word):
    print(word, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


async def main():
    await print_time("开始")
    await wait()
    await print_time("结束")

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()