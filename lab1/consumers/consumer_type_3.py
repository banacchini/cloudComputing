from lab1.consumers.base_consumer import BaseConsumer
import json
from lab1.app.connection import create_connection
from lab1.utils.logger import logger


class ConsumerType3(BaseConsumer):
    def __init__(self):
        super().__init__(queue_name='Type3Event', processing_interval=10)

    def process_event(self, event_data):
        # Custom processing logic for Type3Event
        logger.info(f" [x] Processed Type3Event: {event_data}")

        # Publish a new event after processing
        self.publish_event()

    def publish_event(self):
        connection, channel = create_connection()
        channel.queue_declare(queue='Type4Event')

        event = {"type": "Type4Event", "message": "New Event from Type3Event"}
        channel.basic_publish(exchange='',
                              routing_key='Type4Event',
                              body=json.dumps(event))  # Encode the event as a JSON string
        logger.info(f" [x] Sent '{event}'")

        connection.close()


if __name__ == "__main__":
    consumer = ConsumerType3()
    consumer.start_consuming()