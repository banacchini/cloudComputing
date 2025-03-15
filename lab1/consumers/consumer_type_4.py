from lab1.consumers.base_consumer import BaseConsumer
from lab1.utils.logger import logger


class ConsumerType4(BaseConsumer):
    def __init__(self):
        super().__init__(queue_name='Type4Event', processing_interval=12)

    def process_event(self, event_data):
        # Custom processing logic for Type4Event
        logger.info(f" [x] Processed Type4Event: {event_data}")

if __name__ == "__main__":
    consumer = ConsumerType4()
    consumer.start_consuming()