from tkinter import *
from tkinter import ttk
from datetime import datetime


class HeaderFrame(ttk.Frame):
    def __init__(self, container, style, style_class=""):
        super().__init__(container, style=style_class)

        self.style = style
        self.HEADER_STYLE_CLASS = style_class
        self.DATE_STYLE_CLASS = "Date.Header.TLabel"
        self.TITLE_STYLE_CLASS = "Title.Header.TLabel"
        self.EMPTY_STYLE_CLASS = "Empty.Header.TLabel"

        self.date = StringVar()
        self.title = StringVar()

        self.__configure_style()
        self.__create_widgets()
        self.__render_widgets()

    def __configure_style(self):
        # Header frame bg color
        header_bg_color = self.style.lookup(
            self.HEADER_STYLE_CLASS, "background")
        # Styling options
        date_options = {
            "font": ("Arial", 11, "italic"),
            "background": header_bg_color
        }
        title_options = {
            "font": ("Arial", 14),
            "anchor": "center",
            "background": header_bg_color
        }
        empty_options = {
            "background": header_bg_color
        }

        self.style.configure(self.DATE_STYLE_CLASS, **date_options)
        self.style.configure(self.TITLE_STYLE_CLASS, **title_options)
        self.style.configure(self.EMPTY_STYLE_CLASS, **empty_options)

    def __create_widgets(self):
        # TODO: Create a thread to update current time
        now = datetime.now()
        self.date.set(now.strftime("%H:%M - %d/%m"))
        self.title.set("HOMEPAGE")

        # Current date and time
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
        self.columnconfigure(1, weight=4)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)

        self.date_lbl.grid(row=0, column=0, sticky=(N, S))
        self.title_lbl.grid(row=0, column=1, sticky=(N, S), ipadx=5)
        self.empty_lbl.grid(row=0, column=2, sticky=(N, S), padx=50)
