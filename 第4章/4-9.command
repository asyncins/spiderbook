# 步骤 1，更改 settings.py 中的配置
# 设置调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 设置去重器
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# 更改管道器
ITEM_PIPELINES = {
    'scrapy_redis.pipelines.RedisPipeline': 300
}
# 设置队列
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.PriorityQueue'
# 设置 Redis 连接参数，其中包括用户名、密码、地址和端口号
REDIS_HOST = 'localhost'
REDIS_URL = 'redis://user:pass@hostname:9001'

# 步骤 2，在终端执行
$ scrapy startproject Example
$ cd Example
$ scrapy genspider example example.com

# 步骤 3
from scrapy_redis.spiders import RedisSpider
class ExampleSpider(RedisSpider):
    name = 'example'
		allowed_domains = ['example.com']
    def parse(self, response):
        # do stuff
        pass

# 步骤 4，在终端执行
$ scrapy runspider example.py

# 步骤 5，在 Redis-Client 执行
> lpush example:start_urls http://example.com