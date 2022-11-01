from tkinter import *
from tkinter import ttk


class HomeFrame(ttk.Frame):
    def __init__(self, container, style):

        # Styling options
        options = {'padx': 5, 'pady': 5}
        self.style = style
        self.style.configure('home.TFrame', background='blue')

        super().__init__(container, style="home.TFrame")
