from lab1.consumers.base_consumer import BaseConsumer
from lab1.utils.logger import logger


class ConsumerType2(BaseConsumer):
    def __init__(self):
        super().__init__(queue_name='Type2Event', processing_interval=7)

    def process_event(self, event_data):
        # Custom processing logic for Type2Event
        logger.info(f" [x] Processed Type2Event: {event_data}")
if __name__ == "__main__":
    consumer = ConsumerType2()
    consumer.start_consuming()