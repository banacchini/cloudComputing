import pika
from lab1.app.connection import create_connection


def publish_event(message):
    connection, channel = create_connection()
    channel.queue_declare(queue='my_queue')

    channel.basic_publish(exchange='',
                          routing_key='my_queue',
                          body=message)
    print(f" [x] Sent '{message}'")

    connection.close()


if __name__ == "__main__":
    publish_event('Hello, World!')