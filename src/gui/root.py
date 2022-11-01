from tkinter import *
from tkinter import ttk
from gui.header import HeaderFrame
from gui.homepage import HomeFrame


class OperatorHMI(Tk):
    def __init__(self):
        super().__init__()

        self.ASSETS_PATH = "src/assets/"
        self.IMG_PATH = self.ASSETS_PATH + "imgs/machine.jpg"

        # Window config
        self.title('Operator HMI')
        self.resizable(0, 0)
        self.geometry('750x850')

        # Global styling options
        self.style = ttk.Style(self)
        self.__configure_style()

        # Header frame
        self.header_frame = HeaderFrame(self, self.style)
        self.header_frame.grid(column=0, row=0, sticky=(N, W, E, S))

        # Homepage frame
        self.home_frame = HomeFrame(self, self.style)
        self.home_frame.grid(column=0, row=1, sticky=(N, W, E, S))

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=20)
        self.columnconfigure(0, weight=1)

    def __configure_style(self):
        header_options = {
            "highlightbackground": "blue",
            "highlightthickness": 2
        }
        self.style.configure("header.TFrame", **header_options)
