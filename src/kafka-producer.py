from datetime import datetime
import sys
from time import time

from kafka import KeyedProducer, KafkaClient


def get_time():
    return datetime.fromtimestamp(time()).strftime('%Y-%m-%d %H:%M:%S')


def main():
    # To send messages synchronously
    kafka = KafkaClient('localhost:9092')
    producer = KeyedProducer(kafka)

    # Insure that topic exists
    kafka.ensure_topic_exists('test')

    while True:
        # Note that the application is responsible for encoding messages to type bytes
        producer.send_messages(
            'test',  # topic
            'topic-key',  # key
            'Hello from script!! (time: {})'.format(get_time()),  # message
        )
        input_str = raw_input("Press enter to send another message, otherwise press 'q' to quit: ")

        if input_str and input_str in "qQ":
            sys.exit(0)


if __name__ == "__main__":
    main()
