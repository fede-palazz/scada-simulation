from gui import OperatorHMI
from time import sleep
from confluent_kafka import Consumer
import threading
from time import sleep
#import assets.helloworld_pb2 as HelloWorld
import assets.machine_data_pb2 as MachineData


def checkMessages(topic, app):
    print(topic)
    config = {'bootstrap.servers': 'localhost:9092',
              'group.id': 'consumer_test',
              'auto.offset.reset': 'earliest'}
    # Create Consumer instance
    consumer = Consumer(config)
    # Subscribe to topic
    # topic = "teaming_event"
    # consumer.subscribe([topic], on_assign=reset_offset)
    consumer.subscribe([topic])

    t = threading.current_thread()
    print(type(app))
    # Poll for new messages from Kafka and print them.
    try:
        while getattr(t, "do_run", True):
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
                machine_data = MachineData.MachineDataMessage()
                machine_data.ParseFromString(msg.value())
                # print("Temp: " + str(machine_data.temp))
                # print("Power: " + str(machine_data.power))
                # print("Alarm: " + str(machine_data.alarm))
                # Update UI
                if getattr(t, "do_run", True):
                    app.updateMachineData(machine_data)
                else:
                    break
            sleep(0.1)

    except KeyboardInterrupt:
        pass
    finally:
        # Leave group and commit final offsets
        consumer.close()
        print("Thread stopped")


if __name__ == '__main__':
    app = OperatorHMI()
    t = threading.Thread(target=checkMessages, args=("teaming_event", app,))
    t.start()
    app.mainloop()
    print("Exited mainloop")
    t.do_run = False
