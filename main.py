# Import required libraries
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from time import sleep
from confluent_kafka import Consumer
import threading
from time import sleep
import assets.helloworld_pb2 as HelloWorld


def checkMessages(topic):
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
                hello_proto = HelloWorld.HelloMessage()
                hello_proto.ParseFromString(msg.value())
                print("Name: " + hello_proto.name)
            sleep(0.1)

    except KeyboardInterrupt:
        pass
    finally:
        # Leave group and commit final offsets
        consumer.close()
        print("Thread stopped")


class OperatorHMI(Tk):
    def __init__(self):
        super().__init__()

        self.img_path = "./assets/imgs/machine.jpg"

        # configure the root window
        self.title('Operator HMI')
        self.resizable(0, 0)
        self.geometry('600x500')
        # Set default style
        self.style = ttk.Style(self)
        # Create style used by default for all Frames
        # self.style.configure('TFrame', background='white')

        # Set main frame
        self.mainframe = ttk.Frame(self, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # Title label
        self.title_lbl = ttk.Label(self.mainframe, text="Operator HMI")
        self.title_lbl.grid(column=0, row=0, sticky=(N, W))

        # Img label
        # Create an object of tkinter ImageTk
        self.img = ImageTk.PhotoImage(Image.open(self.img_path))
        # Create a Label Widget to display the text or Image
        self.img_lbl = ttk.Label(self.mainframe, image=self.img)
        self.img_lbl.grid(column=0, row=1, sticky=(N, W))


if __name__ == '__main__':
    app = OperatorHMI()
    # root.after(500, checkMessages, root)
    t = threading.Thread(target=checkMessages, args=("teaming_event",))
    t.start()
    app.mainloop()
    t.do_run = False
