from .base_event import BaseEvent

class EventD(BaseEvent):
    def process(self):
        print("Processing EventD")