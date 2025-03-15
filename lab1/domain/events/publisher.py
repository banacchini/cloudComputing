import json
from lab1.app.connection import create_connection


def publish_event(event_type, message):
    connection, channel = create_connection()
    channel.queue_declare(queue='my_queue')

    event = {"type": event_type, "message": message}
    channel.basic_publish(exchange='',
                          routing_key='my_queue',
                          body=json.dumps(event))
    print(f" [x] Sent '{event}'")

    connection.close()


if __name__ == "__main__":
    publish_event('EventA', 'Hello from EventA')
    publish_event('EventB', 'Hello from EventB')