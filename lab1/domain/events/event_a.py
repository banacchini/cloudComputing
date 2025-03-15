from .base_event import BaseEvent

class EventA(BaseEvent):
    def process(self):
        print("Processing EventA")