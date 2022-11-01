from tkinter import *
from tkinter import ttk
from datetime import datetime


class HeaderFrame(ttk.Frame):
    def __init__(self, container, style):

        self.style = style
        self.date = StringVar()
        self.title = StringVar()

        # Styling options
        self.__configure_style()
        # Initialise Header Frame
        super().__init__(container, style="header.TFrame")

        self.__create_widgets()
        self.__render_widgets()

    def __create_widgets(self):
        # TODO: Create a thread to update current time
        now = datetime.now()
        self.date.set(now.strftime("%H:%M - %d/%m"))
        self.title.set("HOMEPAGE")

        # Current date and time
        self.date_lbl = ttk.Label(
            self, textvariable=self.date,
            style="header.date.TLabel")
        # Current view's title
        self.title_lbl = ttk.Label(
            self, textvariable=self.title,
            style="header.title.TLabel")
        # Used to center title
        self.empty_lbl = ttk.Label(self, text="")

    def __configure_style(self):
        date_options = {"font": ("Arial", 11, "italic")}
        title_options = {
            "font": ("Arial", 14),
            "anchor": "center"
        }

        self.style.configure('header.date.TLabel', **date_options)
        self.style.configure('header.title.TLabel', **title_options)

    def __render_widgets(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=4)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)

        self.date_lbl.grid(row=0, column=0, sticky=(N, S))
        self.title_lbl.grid(row=0, column=1, sticky=(N, S), ipadx=5)
        self.empty_lbl.grid(row=0, column=2, sticky=(N, S), padx=50)
