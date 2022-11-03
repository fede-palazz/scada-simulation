from tkinter import *
from tkinter import ttk


class LastReportedFrame(ttk.Frame):
    def __init__(self, container, style, style_class=""):
        super().__init__(container, style=style_class)

        # Constants

        self.style = style
        self.style_class = style_class
        self.parent = container

        # Initialise widgets
        self.__configure_style()
        self.__create_widgets()
        self.__render_widgets()

    def __configure_style(self):
        pass

    def __create_widgets(self):
        self.btn = ttk.Button(self, text="HOMEPAGE",
                              command=lambda: self.show_homepage())

    def __render_widgets(self):
        self.btn.pack()

    def show_homepage(self):
        self.parent.show_page()
