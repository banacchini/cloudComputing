import json
import time
import random
from lab1.app.connection import create_connection
from lab1.utils.logger import logger


def publish_event():
    connection, channel = create_connection()
    channel.queue_declare(queue='Type2Event')

    while True:
        event = {"type": "Type2Event", "message": "Message from Type2Event"}
        channel.basic_publish(exchange='',
                              routing_key='Type2Event',
                              body=json.dumps(event))  # Encode the event as a JSON string
        logger.info(f" [x] Sent '{event}'")
        time.sleep(random.randint(1, 10))  # Publishing at random intervals


if __name__ == "__main__":
    publish_event()