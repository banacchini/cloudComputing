from .base_event import BaseEvent

class Type2Event(BaseEvent):
    def process(self):
        print("Processing Event Type 2")