from tkinter import *
from tkinter import ttk
from gui.header import HeaderFrame
from gui.homepage import HomeFrame


class OperatorHMI(Tk):
    def __init__(self):
        super().__init__()

        self.ASSETS_PATH = "src/assets/"
        self.IMG_PATH = self.ASSETS_PATH + "imgs/machine.jpg"
        self.HEADER_STYLE_CLASS = "Header.TFrame"

        # Window config
        self.title('Operator HMI')
        self.resizable(0, 0)
        self.geometry('750x850')

        # Global styling options
        self.style = ttk.Style(self)
        self.__configure_style()
        self.__create_widgets()
        self.__render_widgets()

    def __configure_style(self):
        header_options = {
            "background": "green",
        }
        self.style.configure(self.HEADER_STYLE_CLASS, **header_options)
        self.style.configure("Header.TLabel", foreground="white")

    def __create_widgets(self):
        # Header frame
        self.header_frame = HeaderFrame(
            self, self.style, self.HEADER_STYLE_CLASS)

        # Homepage frame
        self.home_frame = HomeFrame(self, self.style)

    def __render_widgets(self):
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=20)
        self.columnconfigure(0, weight=1)

        self.header_frame.grid(column=0, row=0, sticky=(N, W, E, S))
        self.home_frame.grid(column=0, row=1, sticky=(N, W, E, S))
