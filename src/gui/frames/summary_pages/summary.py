from tkinter import *
from tkinter import ttk


class SummaryFrame(ttk.Frame):
    def __init__(self, container, style, style_class=""):
        super().__init__(container, style=style_class)

        # Constants
        self.HEADING_STYLE_CLASS = "Heading.Summary.TLabel"
        self.SUBHEADING_STYLE_CLASS = "SubHeading.Summary.TLabel"
        self.BTN_STYLE_CLASS = "Summary.TButton"
        self.TIME_INTERVAL_OPTIONS = ["30 min", "60 min", "90 min", "120 min"]

        self.style = style
        self.style_class = style_class
        self.parent = container

        # Initialise widgets
        self.__configure_style()
        self.__create_widgets()
        self.__render_widgets()

    def __configure_style(self):
        parent_bg_color = self.style.lookup(
            self.style_class, "background")
        heading_options = {
            "background": parent_bg_color,
            "font": ("Arial", 16, "bold"),
        }
        subheading_options = {
            "background": parent_bg_color,
            "font": ("Arial", 13, "bold"),
        }
        btn_options = {
            "font": ("Arial", 12, "bold")
        }
        self.style.configure(self.HEADING_STYLE_CLASS, **heading_options)
        self.style.configure(self.SUBHEADING_STYLE_CLASS, **subheading_options)
        self.style.configure(self.BTN_STYLE_CLASS, **btn_options)

    def __create_widgets(self):
        self.heading_frame = ttk.Frame(self, style=self.style_class)
        self.time_interval_lbl = ttk.Label(self.heading_frame,
                                           text="TIME INTERVAL",
                                           style=self.SUBHEADING_STYLE_CLASS)
        self.time_interval_cmb = ttk.Combobox(
            self.heading_frame, state="readonly", values=self.TIME_INTERVAL_OPTIONS, style="test.TCombobox")
        # Select first item
        self.time_interval_cmb.current(newindex=0)
        # Resize width
        self.time_interval_cmb.configure(
            width=len(self.time_interval_cmb.get())+5)
        self.home_btn = ttk.Button(self.heading_frame, text="HOMEPAGE",
                                   style=self.BTN_STYLE_CLASS,
                                   command=lambda: self.on_homepage_click())
        self.incident_list_btn = ttk.Button(self.heading_frame, text="LIST VIEW",
                                            style=self.BTN_STYLE_CLASS,
                                            command=lambda: self.on_incident_list_click())
        self.card_view_frame = ttk.Frame(self, style=self.style_class)
        self.list_view_frame = ttk.Frame(self, style=self.style_class)

    def __render_widgets(self):
        # Heading section
        self.heading_frame.pack(fill=X)

        paddings = {"padx": 15, "pady": 10}
        self.time_interval_lbl.pack(
            side=LEFT, expand=True, **paddings)
        self.time_interval_cmb.pack(
            side=LEFT, expand=True, **paddings)
        self.incident_list_btn.pack(
            side=LEFT, expand=True, **paddings)
        self.home_btn.pack(
            side=LEFT, expand=True, **paddings)

        # Body section
        self.card_view_frame.pack(expand=True, fill=BOTH)

    def on_homepage_click(self):
        self.parent.show_page()

    def on_incident_list_click(self):
        pass
