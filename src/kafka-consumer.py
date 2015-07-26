from kafka import KafkaConsumer


def main():
    # To consume messages
    consumer = KafkaConsumer('test',
                             group_id='consumer-script',
                             bootstrap_servers=['localhost:9092'],
                             # auto_offset_reset="smallest",
                             auto_commit_enable=True,
                             auto_commit_interval_ms=1000,
                             auto_commit_interval_messages=1)
    for message in consumer:
        # message value is raw byte string -- decode if necessary!
        # e.g., for unicode: `message.value.decode('utf-8')`
        print("{}:{}:{}: key={} value={}".format(message.topic,
                                                 message.partition,
                                                 message.offset,
                                                 message.key,
                                                 message.value.decode('utf-8')))
        consumer.task_done(message)


if __name__ == "__main__":
    main()
