import threading
import time

from lab1.publishers.base_publisher import BasePublisher
from lab1.utils.logger import logger


class PublisherType1(BasePublisher):
    def __init__(self):
        super().__init__(queue_name='Type1Event', interval=5)

    def start(self):
        threading.Thread(target=self.publish_event, args=('Type1Event', 'Message from Type1Event')).start()


if __name__ == "__main__":
    publisher = PublisherType1()
    publisher.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        publisher.stop()
        logger.info(' [*] PublisherType1 stopped.')