#!/usr/bin/env python

from random import choice
from confluent_kafka import Producer
import assets.helloworld_pb2 as HelloWorld
from time import sleep

if __name__ == '__main__':

    config = {'bootstrap.servers': 'localhost:9092'}

    # Create Producer instance
    producer = Producer(config)

    # Optional per-message delivery callback (triggered by poll() or flush())
    # when a message has been successfully delivered or permanently
    # failed delivery (after retries).
    def delivery_callback(err, msg):
        if err:
            print('ERROR: Message failed delivery: {}'.format(err))
        else:
            print("Produced event to topic {topic}: name = {name}".format(
                topic=msg.topic(), name=msg.value()))

    # Produce data by selecting random values from these lists.
    topic = "teaming_event"
    names = ['eabara', 'jsmith', 'sgarcia',
             'jbernard', 'htanaka', 'awalther']

    count = 0
    for _ in range(10):
        rand_name = choice(names)
        hello_proto = HelloWorld.HelloMessage(name=rand_name)
        serialized = hello_proto.SerializeToString()
        # produce(topic, value, key, callback)
        # producer.produce(topic, product, user_id, callback=delivery_callback)
        producer.produce(topic=topic, value=serialized,
                         callback=delivery_callback)
        count += 1
        # Block until the messages are sent.
        producer.poll(10000)
        producer.flush()
        sleep(1)
