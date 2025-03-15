import json
import time
from lab1.app.connection import create_connection
from lab1.domain.events.event_type_3 import Type3Event
from lab1.domain.events.event_type_4 import Type4Event
from lab1.utils.logger import logger


def callback(ch, method, properties, body):
    event_data = json.loads(body)  # Decode the JSON string back into a Python dictionary
    event_instance = Type3Event()
    event_instance.process()
    logger.info(f" [x] Processed '{event_data}'")

    # Simulate processing time
    time.sleep(10)

    # Publish a new event after processing
    publish_event()


def publish_event():
    connection, channel = create_connection()
    channel.queue_declare(queue='Type4Event')

    event = {"type": "Type4Event", "message": "New Event from Type3Event"}
    channel.basic_publish(exchange='',
                          routing_key='Type4Event',
                          body=json.dumps(event))  # Encode the event as a JSON string
    logger.info(f" [x] Sent '{event}'")

    connection.close()


def consume_events():
    connection, channel = create_connection()
    channel.queue_declare(queue='Type3Event')

    channel.basic_consume(queue='Type3Event',
                          on_message_callback=callback,
                          auto_ack=True)

    logger.info(' [*] Waiting for messages. To exit press CTRL+C')
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        logger.info(' [*] Exiting...')
    finally:
        connection.close()


if __name__ == "__main__":
    consume_events()