from .base_event import BaseEvent

class EventC(BaseEvent):
    def process(self):
        print("Processing EventC")