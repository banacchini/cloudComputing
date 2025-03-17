from lab1_repair.publishers_project.app.publisher_service import create_type2_publisher
from lab1_repair.shared.domain.events.events_data import Type2Event

def start_publisher():
    publisher = create_type2_publisher()
    publisher.publish_event(Type2Event("Event data for Type2"))

if __name__ == "__main__":
    start_publisher()