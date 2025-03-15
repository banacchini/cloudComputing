import random
import threading
import time

from lab1.publishers.base_publisher import BasePublisher
from lab1.utils.logger import logger


class PublisherType2(BasePublisher):
    def __init__(self):
        super().__init__(queue_name='Type2Event', interval=random.randint(3, 10))

    def start(self):
        threading.Thread(target=self.publish_event, args=('Type2Event', 'Message from Type2Event')).start()


if __name__ == "__main__":
    publisher = PublisherType2()
    publisher.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        publisher.stop()
        logger.info(' [*] PublisherType2 stopped.')