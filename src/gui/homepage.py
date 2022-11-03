from tkinter import *
from tkinter import ttk


class HomeFrame(ttk.Frame):
    def __init__(self, container, style, style_class=""):
        super().__init__(container, style=style_class)

        # Constants
        self.BTN_STYLE_CLASS = "Home.TButton"

        self.style = style
        self.style_class = style_class
        self.parent = container

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
        self.summary_btn = ttk.Button(
            self, text="REPORTED INCIDENTS", style=self.BTN_STYLE_CLASS)
        # Report part incident btn
        self.part_btn = ttk.Button(
            self, text="REPORT PART INCIDENT", style=self.BTN_STYLE_CLASS)
        # Report machine incident btn
        self.machine_btn = ttk.Button(
            self, text="REPORT MACHINE INCIDENT",
            style=self.BTN_STYLE_CLASS)
        # Report last reported incident
        self.last_reported_btn = ttk.Button(
            self, text="REPORT LAST REPORTED INCIDENT", style=self.BTN_STYLE_CLASS)

        # Assign btn commands
        self.summary_btn.configure(
            command=lambda: self.parent.show_page("SummaryFrame"))
        self.part_btn.configure(
            command=lambda: self.parent.show_page("PartFrame"))
        self.machine_btn.configure(
            command=lambda: self.parent.show_page("MachineFrame"))
        self.last_reported_btn.configure(
            command=lambda: self.parent.show_page("LastReportedFrame"))

    def __render_widgets(self):
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=2)
        self.rowconfigure(2, weight=2)
        self.rowconfigure(3, weight=2)
        self.rowconfigure(4, weight=2)
        self.rowconfigure(5, weight=1)
        self.columnconfigure(0, weight=1)

        paddings = {"ipadx": 20, "ipady": 10}
        self.summary_btn.grid(
            row=1, column=0, **paddings)
        self.part_btn.grid(
            row=2, column=0, **paddings)
        self.machine_btn.grid(
            row=3, column=0, **paddings)
        self.last_reported_btn.grid(
            row=4, column=0, **paddings)
