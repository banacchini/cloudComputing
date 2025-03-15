import random
import threading
import time

from lab1.publishers.base_publisher import BasePublisher
from lab1.utils.logger import logger


class PublisherType3(BasePublisher):
    def __init__(self):
        super().__init__(queue_name='Type3Event', interval=random.randint(3, 10))

    def start(self):
        threading.Thread(target=self.publish_event, args=('Type3Event', 'Message from Type3Event')).start()


if __name__ == "__main__":
    publisher = PublisherType3()
    publisher.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        publisher.stop()
        logger.info(' [*] PublisherType3 stopped.')