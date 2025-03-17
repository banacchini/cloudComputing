import time
import random
from lab1_repair.shared.utils.logger import logger
from lab1_repair.shared.domain.events.events_data import Type1Event, Type2Event, Type3Event
from lab1_repair.shared.connection.queue_connection import create_connection

class BasePublisher:
    def __init__(self, queue_name, interval_min, interval_max):
        self.connection, self.channel = create_connection()
        self.channel.queue_declare(queue=queue_name)
        self.queue_name = queue_name
        self.interval_min = interval_min
        self.interval_max = interval_max
        self.running = True

    def publish_event(self, event):
        while self.running:
            self.channel.basic_publish(exchange='',
                                       routing_key=self.queue_name,
                                       body=str(event))
            logger.info(f" [x] Sent '{event}'")
            time.sleep(random.randint(self.interval_min, self.interval_max))

    def stop(self):
        self.running = False
        self.connection.close()

def create_type1_publisher():
    return BasePublisher("Type1Event", 5, 5)

def create_type2_publisher():
    return BasePublisher("Type2Event", 2, 6)

def create_type3_publisher():
    return BasePublisher("Type3Event", 4, 8)