from lab1_repair.consumers_project.app.consumer_service import create_type4_consumer

def start_consumer():
    consumer = create_type4_consumer()
    consumer.start_consuming()

if __name__ == "__main__":
    start_consumer()