from lab1_repair.publishers_project.app.publisher_service import create_type2_publisher
from lab1_repair.shared.domain.events.events_data import Type3Event

def start_publisher():
    publisher = create_type2_publisher()
    publisher.publish_event(Type3Event("Event data for Type3"))

if __name__ == "__main__":
    start_publisher()