import requests

# 创建一个集合，作为增量池
after = set()
# 设定 URL 列表
urls = ["http://www.example.com?page=1&id=2r9l74hjng",
        "http://www.example.com?page=1&id=9kiujamzj6",
        "http://www.example.com?page=1&id=77274jnasf",
        "http://www.example.com?page=1&id=9kiujamzj6"
]
# 循环 URL 列表
for url in urls:
    # 条件判断
    if url not in after:
            # 如果 URL 不在增量池中则向目标网页发出请求
            resp = requests.get(url)
            # 发出请求后，将 URL 添加到增量池
            after.add(url)
    else:
        # 不作处理
        pass
print(len(after), after)