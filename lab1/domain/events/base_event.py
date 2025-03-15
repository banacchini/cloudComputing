class BaseEvent:
    def process(self):
        raise NotImplementedError("Subclasses should implement this method.")