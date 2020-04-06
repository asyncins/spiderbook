import pika


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


auth = pika.PlainCredentials("books", "spider")
connection = pika.BlockingConnection(pika.ConnectionParameters('148.70.6*.5*', 5672, "/", auth))
channel = connection.channel()
channel.basic_consume(
    queue='message_box', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()