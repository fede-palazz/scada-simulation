from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image


class OperatorHMI(Tk):
    def __init__(self):
        super().__init__()

        self.ASSETS_PATH = "assets/"
        self.IMG_PATH = self.ASSETS_PATH + "imgs/machine.jpg"

        # configure the root window
        self.title('Operator HMI')
        self.resizable(0, 0)
        self.geometry('700x600')
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
        self.title_lbl = ttk.Label(
            self.mainframe, text="Operator HMI", font=("Arial", 25))
        self.title_lbl.grid(column=0, row=0, sticky=(N, W), pady=(10, 30))

        # Img label
        # Create an object of tkinter ImageTk
        self.img = ImageTk.PhotoImage(Image.open(self.IMG_PATH))
        # Create a Label Widget to display the text or Image
        self.img_lbl = ttk.Label(self.mainframe, image=self.img, width=80)
        self.img_lbl.grid(column=0, row=1, sticky=(N, W), pady=(5, 25))

        # Temp label
        self.temp_lbl = ttk.Label(
            self.mainframe, text="Temp: [°C]", font=("Arial", 14))
        self.temp_lbl.grid(column=0, row=2, sticky=(N, W),
                           pady=(10, 10), padx=10)

        # Power label
        self.power_lbl = ttk.Label(
            self.mainframe, text="Power: [W]", font=("Arial", 14))
        self.power_lbl.grid(column=0, row=3, sticky=(N, W),
                            pady=(10, 10), padx=10)

        # Alarm label
        self.alarm_lbl = ttk.Label(
            self.mainframe, text="Alarm: ", font=("Arial", 14))
        self.alarm_lbl.grid(column=0, row=4, sticky=(N, W),
                            pady=(10, 10), padx=10)

    def updateMachineData(self, data):
        self.temp_lbl["text"] = f"Temp: {str(round(data.temp, 2))} [°C]"
        self.power_lbl["text"] = f"Power: {str(round(data.power, 2))} [W]"
        self.alarm_lbl["text"] = f"Alarm: {str(data.alarm)}"
