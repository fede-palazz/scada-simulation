#!/usr/bin/env python

from random import choice
from confluent_kafka import Producer
#import assets.helloworld_pb2 as HelloWorld
import assets.machine_data_pb2 as MachineData
from time import sleep
import random


def getRandomTemp():
    return round((random.random()*100+10), 2)


def getRandomPower():
    return round((random.random()*1000+100), 2)


def getRandomAlarm():
    return bool(random.getrandbits(1))


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
            print("Produced event to topic {topic}: data = {data}".format(
                topic=msg.topic(), data=msg.value()))

    # Produce data by selecting random values from these lists.
    topic = "teaming_event"
    names = ['eabara', 'jsmith', 'sgarcia',
             'jbernard', 'htanaka', 'awalther']

    count = 0
    for _ in range(100):
        #rand_name = choice(names)
        machine_data = MachineData.MachineDataMessage(
            temp=getRandomTemp(),
            power=getRandomPower(),
            alarm=getRandomAlarm())
        serialized = machine_data.SerializeToString()
        # produce(topic, value, key, callback)
        # producer.produce(topic, product, user_id, callback=delivery_callback)
        producer.produce(topic=topic, value=serialized,
                         callback=delivery_callback)
        count += 1
        # Block until the messages are sent.
        producer.poll(10000)
        producer.flush()
        sleep(1)
