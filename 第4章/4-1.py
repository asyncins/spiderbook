import requests


# 假设几个爬取目标的 URL
url1 = "http://example.com?x=1"
url2 = "http://example.com?x=2"
url3 = "http://example.com?x=3"

# 初始化待爬队列 before 和已爬队列 after
before = set()
after = set()

# 模拟爬虫程序将 URL 存储到待爬队列
before.add(url1)
before.add(url2)
before.add(url3)

# 打印队列长度
print("未向目标 URL 发出请求时，待爬队列的长度为 %s，已爬队列的长度为 %s" % (len(before), len(after)))

while len(before):
    # 模拟爬虫程序从待爬队列中取出 URL
    request_url = before.pop()
    # 模拟爬虫程序请求 URL
    resp = requests.get(request_url)
    # 模拟爬虫程序将 URL 放入已爬队列
    after.add(request_url)

# 打印队列长度
print("完成请求后，待爬队列的长度为 %s，已爬队列的长度为 %s" % (len(before), len(after)))