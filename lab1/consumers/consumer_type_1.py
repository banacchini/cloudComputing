import json
from lab1.app.connection import create_connection
from lab1.domain.events.event_type_1 import Type1Event
from lab1.utils.logger import logger


def callback(ch, method, properties, body):
    event_data = json.loads(body)  # Decode the JSON string back into a Python dictionary
    event_instance = Type1Event()
    event_instance.process()
    logger.info(f" [x] Processed '{event_data}'")


def consume_events():
    connection, channel = create_connection()
    channel.queue_declare(queue='Type1Event')

    channel.basic_consume(queue='Type1Event',
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