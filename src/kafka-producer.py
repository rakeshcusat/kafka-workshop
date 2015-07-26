from kafka import KeyedProducer, KafkaClient


def main():
    # To send messages synchronously
    kafka = KafkaClient('localhost:9092')
    producer = KeyedProducer(kafka)

    # Insure that topic exists
    kafka.ensure_topic_exists('test')
    # Note that the application is responsible for encoding messages to type bytes
    producer.send_messages(b'test',  b'topic-key', b'Hello from script')


if __name__ == "__main__":
    main()
