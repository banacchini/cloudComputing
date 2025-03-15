from .base_event import BaseEvent

class EventB(BaseEvent):
    def process(self):
        print("Processing EventB")