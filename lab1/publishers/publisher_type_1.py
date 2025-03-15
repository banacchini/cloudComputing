import json
import time
from lab1.app.connection import create_connection
from lab1.utils.logger import logger

TIME_TO_SLEEP = 5

def publish_event():
    connection, channel = create_connection()
    channel.queue_declare(queue='Type1Event')

    while True:
        event = {"type": "Type1Event", "message": "Message from Type1Event"}
        channel.basic_publish(exchange='',
                              routing_key='Type1Event',
                              body=json.dumps(event))  # Encode the event as a JSON string
        logger.info(f" [x] Sent '{event}'")
        time.sleep(TIME_TO_SLEEP)  # Publishing at regular intervals


if __name__ == "__main__":
    publish_event()