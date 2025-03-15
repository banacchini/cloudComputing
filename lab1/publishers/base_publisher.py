import json
import time
from lab1.app.connection import create_connection
from lab1.utils.logger import logger

class BasePublisher:
    def __init__(self, queue_name, interval):
        self.connection, self.channel = create_connection()
        self.channel.queue_declare(queue=queue_name)
        self.queue_name = queue_name
        self.interval = interval
        self.running = True

    def publish_event(self, event_type, message):
        while self.running:
            event = {"type": event_type, "message": message}
            self.channel.basic_publish(exchange='',
                                       routing_key=self.queue_name,
                                       body=json.dumps(event))  # Encode the event as a JSON string
            logger.info(f" [x] Sent '{event}'")
            time.sleep(self.interval)  # Publishing at regular intervals

    def stop(self):
        self.running = False
        self.connection.close()