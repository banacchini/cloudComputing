import json
import time
import threading
import random
from lab1.app.connection import create_connection
from lab1.utils.logger import logger


class PublisherType2:
    def __init__(self):
        self.connection, self.channel = create_connection()
        self.channel.queue_declare(queue='Type2Event')
        self.running = True

    def publish_event(self):
        while self.running:
            event = {"type": "Type2Event", "message": "Message from Type2Event"}
            self.channel.basic_publish(exchange='',
                                       routing_key='Type2Event',
                                       body=json.dumps(event))  # Encode the event as a JSON string
            logger.info(f" [x] Sent '{event}'")
            interval = random.randint(1, 10)  # Random interval for each message
            time.sleep(interval)  # Publishing at random intervals

    def stop(self):
        self.running = False
        self.connection.close()

    def start(self):
        threading.Thread(target=self.publish_event).start()


if __name__ == "__main__":
    publisher = PublisherType2()
    publisher.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        logger.info(' [*] Stopping publisher...')
        publisher.stop()
        logger.info(' [*] PublisherType2 stopped.')