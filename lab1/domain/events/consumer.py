from lab1.app.connection import create_connection


def callback(ch, method, properties, body):
    print(f" [x] Received {body}")


def consume_events():
    connection, channel = create_connection()
    channel.queue_declare(queue='my_queue')

    channel.basic_consume(queue='my_queue',
                          on_message_callback=callback,
                          auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        print(' [*] Exiting...')
    finally:
        connection.close()


if __name__ == "__main__":
    consume_events()