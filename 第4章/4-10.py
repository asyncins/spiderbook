import pika


auth = pika.PlainCredentials("books", "spider")
connection = pika.BlockingConnection(pika.ConnectionParameters('148.70.6*.5*', 5672, "/", auth))

channel = connection.channel()
channel.queue_declare(queue='message_box')
for i in range(5):
    channel.basic_publish(exchange='',
                          routing_key='message_box',
                          body='Hello World-{}'.format(i))
    print(" [x] Sent 'Hello World-{}'".format(i))
connection.close()