import time
import string
import random
import asyncio
import aiomysql


async def test_example_execute(loop):
    # 填写参数，以连接数据库
    conn = await aiomysql.connect(host='127.0.0.1', port=3306,
                                       user='root', password='******',
                                       db='football', loop=loop,
                                       autocommit=True)
    async with conn.cursor() as cur:
        # 循环 50 万次
        for i in range(500000):
            base_url = "http://www.******.com"
            # 生成 6 位的随机小写字母组合
            article = ''.join(random.choices(string.ascii_lowercase, k=6))
            # 生成时间戳
            timestamp = int(time.time())
            # 生成 sign 参数
            sign = article + str(timestamp * 3)
            # 拼接成常见的 URL
            url = "%s?page=1&article=%s&sign=%s&times=%s" % (base_url, article, sign, timestamp)
            # SQL 语句
            query = "INSERT INTO player(url) VALUES ('%s');" % url
            # 执行指定的 SQL 语句
            await cur.execute(query)
    conn.close()


loop = asyncio.get_event_loop()
loop.run_until_complete(test_example_execute(loop))