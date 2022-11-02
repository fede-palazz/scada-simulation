from tkinter import *
from tkinter import ttk


class HomeFrame(ttk.Frame):
    def __init__(self, container, style, style_class=""):
        super().__init__(container, style=style_class)

        # Constants
        self.BTN_STYLE_CLASS = "Home.TButton"

        self.style = style
        self.style_class = style_class

        # Initialise widgets
        self.__configure_style()
        self.__create_widgets()
        self.__render_widgets()

    def __configure_style(self):
        btn_options = {
            "font": ("Arial", 15),
        }
        # Styling options
        self.style.configure(self.BTN_STYLE_CLASS, **btn_options)

    def __create_widgets(self):
        # Reported incident summary btn
        self.reported_summary_btn = ttk.Button(
            self, text="REPORTED INCIDENTS", style=self.BTN_STYLE_CLASS)
        # Report machine incident btn
        self.report_machine_btn = ttk.Button(
            self, text="REPORT MACHINE INCIDENT", style=self.BTN_STYLE_CLASS)
        # Report part incident btn
        self.report_part_btn = ttk.Button(
            self, text="REPORT PART INCIDENT", style=self.BTN_STYLE_CLASS)
        # Report last reported incident
        self.report_last_btn = ttk.Button(
            self, text="REPORT LAST REPORTED INCIDENT", style=self.BTN_STYLE_CLASS)

    def __render_widgets(self):
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=2)
        self.rowconfigure(2, weight=2)
        self.rowconfigure(3, weight=2)
        self.rowconfigure(4, weight=2)
        self.rowconfigure(5, weight=1)

        paddings = {"ipadx": 20, "ipady": 10}
        self.reported_summary_btn.grid(
            row=1, column=0, **paddings)
        self.report_machine_btn.grid(row=2, column=0, **paddings)
        self.report_part_btn.grid(row=3, column=0, **paddings)
        self.report_last_btn.grid(row=4, column=0, **paddings)
