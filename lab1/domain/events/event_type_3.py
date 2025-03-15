from .base_event import BaseEvent

class Type3Event(BaseEvent):
    def process(self):
        print("Processing Event Type 3")