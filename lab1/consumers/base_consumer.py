import json
import time
import threading
from lab1.app.connection import create_connection
from lab1.utils.logger import logger


class BaseConsumer:
    def __init__(self, queue_name, processing_interval):
        self.connection, self.channel = create_connection()
        self.queue_name = queue_name
        self.processing_interval = processing_interval
        self.running = True

    def callback(self, ch, method, properties, body):
        event_data = json.loads(body)  # Decode the JSON string back into a Python dictionary
        self.process_event(event_data)
        logger.info(f" [x] Processed '{event_data}'")

        # Simulate processing time
        time.sleep(self.processing_interval)

    def process_event(self, event_data):
        raise NotImplementedError("Subclasses should implement this method.")

    def start_consuming(self):
        self.channel.queue_declare(queue=self.queue_name)

        self.channel.basic_consume(queue=self.queue_name,
                                   on_message_callback=self.callback,
                                   auto_ack=True)

        logger.info(f' [*] Waiting for messages in {self.queue_name}. To exit press CTRL+C')
        try:
            self.channel.start_consuming()
        except KeyboardInterrupt:
            logger.info(' [*] Exiting...')
        finally:
            self.stop()

    def stop(self):
        self.running = False
        self.connection.close()