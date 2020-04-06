import pika
from pymongo import MongoClient

# 连接 RabbitMQ
auth = pika.PlainCredentials("books", "spider")
connection = pika.BlockingConnection(pika.ConnectionParameters('148.70.6*.5*', 5672, "/", auth))
channel = connection.channel()
queue = "dcs"


# 连接 MongoDB
client = MongoClient('localhost', 27017)
db = client.news
detail = db.detail