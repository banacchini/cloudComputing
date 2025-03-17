# class BaseEvent:
#     def process(self):
#         raise NotImplementedError("Subclasses should implement this method.")
#
# class Type1Event(BaseEvent):
#     def process(self):
#         print("Processing Event Type 1")
#
# class Type2Event(BaseEvent):
#     def process(self):
#         print("Processing Event Type 2")
#
# class Type3Event(BaseEvent):
#     def process(self):
#         print("Processing Event Type 3")
#
# class Type4Event(BaseEvent):
#     def process(self):
#         print("Processing Event Type 4")

class BaseEvent:
    def __init__(self, event_type, data):
        self.event_type = event_type
        self.data = data

    def __str__(self):
        return f"{self.event_type}: {self.data}"

class Type1Event(BaseEvent):
    def __init__(self, data):
        super().__init__("Type1Event", data)

class Type2Event(BaseEvent):
    def __init__(self, data):
        super().__init__("Type2Event", data)

class Type3Event(BaseEvent):
    def __init__(self, data):
        super().__init__("Type3Event", data)

class Type4Event(BaseEvent):
    def __init__(self, data):
        super().__init__("Type4Event", data)