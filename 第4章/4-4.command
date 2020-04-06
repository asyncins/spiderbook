# Redis
# 插入数据
> SADD WaitCrawl mysql
(integer) 1
> SADD WaitCrawl redis
(integer) 1
> SADD WaitCrawl mongodb
(integer) 1
> SADD WaitCrawl sqlite
(integer) 1
> SADD WaitCrawl redis
(integer) 0
# 查询集合
> SMEMBERS WaitCrawl
1) "redis"
2) "sqlite"
3) "mongodb"
4) "mysql"