#!/usr/bin/env python

from confluent_kafka import Consumer, OFFSET_BEGINNING
import assets.helloworld_pb2 as HelloWorld

if __name__ == '__main__':

    config = {'bootstrap.servers': 'localhost:9092',
              'group.id': 'consumer_test',
              'auto.offset.reset': 'earliest'}

    # Create Consumer instance
    consumer = Consumer(config)

    # Set up a callback to handle the '--reset' flag.
    # def reset_offset(consumer, partitions):
    #     # if args.reset:
    #     for p in partitions:
    #         p.offset = OFFSET_BEGINNING
    #     consumer.assign(partitions)

    # Subscribe to topic
    topic = "teaming_event"
    # consumer.subscribe([topic], on_assign=reset_offset)
    consumer.subscribe([topic])
    # Poll for new messages from Kafka and print them.
    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                # Initial message consumption may take up to
                # `session.timeout.ms` for the consumer group to
                # rebalance and start consuming
                print("Waiting...")
            elif msg.error():
                print("ERROR: %s".format(msg.error()))
            else:
                print('Received: ' + str(msg.value()))
                hello_proto = HelloWorld.HelloMessage()
                hello_proto.ParseFromString(msg.value())
                print("Name: " + hello_proto.name)

                # Extract the (optional) key and value, and print.
                # print("Consumed event from topic {topic}: key = {key:12} value = {value:12}".format(
                #     topic=msg.topic(), key=msg.key().decode('utf-8'), value=msg.value().decode('utf-8')))
    except KeyboardInterrupt:
        pass
    finally:
        # Leave group and commit final offsets
        consumer.close()
