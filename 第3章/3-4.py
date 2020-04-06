import time
import string
import random
import pymongo


# 连接 MongoDB
client = pymongo.MongoClient("localhost", 27017)
# 使用 test 数据库
db = client.test


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
    # 往 mongodb 集合中插入数据
    db.sfhfpc.insert_one({article: url})