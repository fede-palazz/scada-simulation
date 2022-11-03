from tkinter import *
from tkinter import ttk
from datetime import datetime


class HeaderFrame(ttk.Frame):
    def __init__(self, container, style, style_class=""):
        super().__init__(container, style=style_class)

        # Constants
        self.DEFAULT_TITLE = "INCIDENT REPORT"
        self.TIME_STYLE_CLASS = "Time.Header.TLabel"
        self.DATE_STYLE_CLASS = "Date.Header.TLabel"
        self.TITLE_STYLE_CLASS = "Title.Header.TLabel"
        self.EMPTY_STYLE_CLASS = "Empty.Header.TLabel"

        self.style = style
        self.style_class = style_class
        # Labels values
        self.date = StringVar()
        self.time = StringVar()
        self.title = StringVar()

        # Initialise widgets
        self.__configure_style()
        self.__create_widgets()
        self.__render_widgets()

    def __configure_style(self):
        # Header frame bg color
        header_bg_color = self.style.lookup(
            self.style_class, "background")
        # Styling options
        time_options = {
            "font": ("Arial", 14, "bold"),
            "background": header_bg_color
        }
        date_options = {
            "font": ("Arial", 12, "italic"),
            "background": header_bg_color
        }
        title_options = {
            "font": ("Comics Sans MS", 18),
            "anchor": "center",
            "background": header_bg_color
        }
        empty_options = {
            "background": header_bg_color
        }

        self.style.configure(self.TIME_STYLE_CLASS, **time_options)
        self.style.configure(self.DATE_STYLE_CLASS, **date_options)
        self.style.configure(self.TITLE_STYLE_CLASS, **title_options)
        self.style.configure(self.EMPTY_STYLE_CLASS, **empty_options)

    def __create_widgets(self):
        # TODO: Create a thread to update current time
        now = datetime.now()
        self.time.set(now.strftime("%H:%M "))
        self.date.set(now.strftime(" %d/%m"))
        self.title.set(self.DEFAULT_TITLE)

        # Current date and time
        self.time_lbl = ttk.Label(
            self, textvariable=self.time,
            style=self.TIME_STYLE_CLASS)
        self.date_lbl = ttk.Label(
            self, textvariable=self.date,
            style=self.DATE_STYLE_CLASS)
        # Current view's title
        self.title_lbl = ttk.Label(
            self, textvariable=self.title,
            style=self.TITLE_STYLE_CLASS)
        # Used to center title
        self.empty_lbl = ttk.Label(self, text="", style=self.EMPTY_STYLE_CLASS)

    def __render_widgets(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=4)
        self.columnconfigure(3, weight=2)
        self.rowconfigure(0, weight=1)

        self.time_lbl.grid(row=0, column=0, sticky=(N, S, E))
        self.date_lbl.grid(row=0, column=1, sticky=(N, S, W),
                           padx=(0, 0))
        self.title_lbl.grid(row=0, column=2, sticky=(N, S),
                            ipadx=5)
        self.empty_lbl.grid(row=0, column=3, sticky=(N, S), padx=62)
