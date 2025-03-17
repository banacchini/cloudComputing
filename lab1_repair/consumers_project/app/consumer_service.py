import time
from lab1_repair.shared.utils.logger import logger
from lab1_repair.shared.domain.events.events_data import Type1Event, Type2Event, Type3Event, Type4Event
from lab1_repair.shared.connection.queue_connection import create_connection

class BaseConsumer:
    def __init__(self, queue_name, processing_interval):
        self.connection, self.channel = create_connection()
        self.channel.queue_declare(queue=queue_name)
        self.queue_name = queue_name
        self.processing_interval = processing_interval
        self.running = True

    def process_event(self, event_data):
        pass

    def start_consuming(self):
        while self.running:
            method_frame, header_frame, body = self.channel.basic_get(self.queue_name)
            if method_frame:
                logger.info(f" [x] Received {body}")
                self.process_event(body)
                self.channel.basic_ack(method_frame.delivery_tag)
            time.sleep(self.processing_interval)

    def stop(self):
        self.running = False
        self.connection.close()

class Type1Consumer(BaseConsumer):
    def process_event(self, event_data):
        logger.info(f"Processed Type1Event: {event_data}")

class Type2Consumer(BaseConsumer):
    def process_event(self, event_data):
        logger.info(f"Processed Type2Event: {event_data}")

class Type3Consumer(BaseConsumer):
    def process_event(self, event_data):
        logger.info(f"Processed Type3Event: {event_data}")
        self.publish_event(Type4Event(data="Generated from Type3Event"))

    def publish_event(self, event):
        self.channel.basic_publish(exchange='',
                                   routing_key="Type4Event",
                                   body=str(event))
        logger.info(f" [x] Sent '{event}'")

class Type4Consumer(BaseConsumer):
    def process_event(self, event_data):
        logger.info(f"Processed Type4Event: {event_data}")

def create_type1_consumer():
    return Type1Consumer("Type1Event", 5)

def create_type2_consumer():
    return Type2Consumer("Type2Event", 5)

def create_type3_consumer():
    return Type3Consumer("Type3Event", 5)

def create_type4_consumer():
    return Type4Consumer("Type4Event", 5)