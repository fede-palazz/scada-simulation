from tkinter import *
from tkinter import ttk


class MachineFrame(ttk.Frame):
    def __init__(self, container, style, style_class=""):
        super().__init__(container, style=style_class)

        # Constants

        self.style = style
        self.style_class = style_class

        # Initialise widgets
        self.__configure_style()
        self.__create_widgets()
        self.__render_widgets()

    def __configure_style(self):
        pass

    def __create_widgets(self):
        pass

    def __render_widgets(self):
        pass