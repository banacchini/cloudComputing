from lab1_repair.publishers_project.app.publisher_service import create_type1_publisher
from lab1_repair.shared.domain.events.events_data import Type1Event

def start_publisher():
    publisher = create_type1_publisher()
    publisher.publish_event(Type1Event("Event data for Type1"))

if __name__ == "__main__":
    start_publisher()