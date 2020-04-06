from pybloom_live import BloomFilter

# 初始化 BloomFilter 对象，设定容量为 1000，误判几率 0.001
f = BloomFilter(capacity=1000, error_rate=0.001)
# 循环将 0～4 的数字添加到 vector 中，并打印返回结果
res = [f.add(x) for x in range(5)]
print(res)
# 单独将数字 4 添加到 vector 中，并打印返回结果
print(f.add(3))
# 判断数字 10 和数字 5 是否在 vector 中，并打印判断结果
print(10 in f)
print(5 in f)