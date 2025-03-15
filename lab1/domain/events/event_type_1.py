from .base_event import BaseEvent

class Type1Event(BaseEvent):
    def process(self):
        print("Processing Event Type 1")