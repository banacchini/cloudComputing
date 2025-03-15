from lab1.consumers.base_consumer import BaseConsumer
from lab1.utils.logger import logger


class ConsumerType1(BaseConsumer):
    def __init__(self):
        super().__init__(queue_name='Type1Event', processing_interval=5)

    def process_event(self, event_data):
        # Custom processing logic for Type1Event
        logger.info(f" [x] Processed Type1Event: {event_data}")
if __name__ == "__main__":
    consumer = ConsumerType1()
    consumer.start_consuming()