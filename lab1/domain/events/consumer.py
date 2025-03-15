import json
from lab1.app.connection import create_connection
from lab1.domain.events.base_event import BaseEvent
from lab1.domain.events.event_a import EventA
from lab1.domain.events.event_b import EventB


def callback(ch, method, properties, body):
    event_data = json.loads(body)  # Decode the JSON string back into a Python dictionary
    event_type = event_data['type']
    message = event_data['message']

    try:
        # Use reflection to dynamically handle different types of events
        event_class = globals()[event_type]
        if issubclass(event_class, BaseEvent):
            event_instance = event_class()
            event_instance.process()
        else:
            print(f" [!] {event_type} is not a valid event class.")
    except KeyError:
        print(f" [!] Event class {event_type} not found.")
    except Exception as e:
        print(f" [!] Error processing event: {e}")


def consume_events():
    connection, channel = create_connection()
    channel.queue_declare(queue='my_queue')

    channel.basic_consume(queue='my_queue',
                          on_message_callback=callback,
                          auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        print(' [*] Exiting...')
    finally:
        connection.close()


if __name__ == "__main__":
    consume_events()