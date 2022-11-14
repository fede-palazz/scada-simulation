from tkinter import *
from tkinter import ttk


class SummaryFrame(ttk.Frame):
    def __init__(self, container, style, style_class=""):
        super().__init__(container, style=style_class)

        # Constants
        self.HEADER_STYLE_CLASS = "Header.Summary.TFrame"
        self.BODY_STYLE_CLASS = "Body.Summary.TFrame"
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
            "font": ("Arial", 14, "bold"),
        }
        subheading_options = {
            # "background": parent_bg_color,
            "font": ("Arial", 12, "bold"),
        }
        btn_options = {
            "font": ("Arial", 12, "bold")
        }
        self.style.configure(self.HEADING_STYLE_CLASS, **heading_options)
        self.style.configure(self.SUBHEADING_STYLE_CLASS, **subheading_options)
        self.style.configure(self.BTN_STYLE_CLASS, **btn_options)

    def __create_widgets(self):
        self.heading_frame = ttk.Frame(self, style=self.HEADER_STYLE_CLASS)
        self.time_interval_lbl = ttk.Label(self.heading_frame,
                                           text="TIME INTERVAL",
                                           style="Title.Summary.TLabel")
        self.style.configure("Title.Summary.TLabel",
                             font=("Arial", 12, "bold"),
                             background="lightgrey")
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
        self.card_view_frame = ttk.Frame(self, style=self.BODY_STYLE_CLASS)
        self.list_view_frame = ttk.Frame(self, style=self.BODY_STYLE_CLASS)

    def __render_widgets(self):
        # Heading section
        self.heading_frame.pack(fill=X)

        paddings = {"padx": 12, "pady": 12}
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
        ttk.Label(self.card_view_frame, style=self.HEADING_STYLE_CLASS,
                  text="INCIDENT SUMMARY").pack(pady=30)
        # Incident summary frame
        incident_summary_frame = ttk.Frame(
            self.card_view_frame, style="Incident.Summary.TFrame")
        self.style.configure("Incident.Summary.TFrame", background="lightgrey")
        incident_summary_frame.columnconfigure(0, weight=2)
        incident_summary_frame.columnconfigure(1, weight=1)
        incident_summary_frame.columnconfigure(2, weight=2)
        incident_summary_frame.rowconfigure(0, weight=1)
        incident_summary_frame.pack(fill=X, expand=True, anchor=N)

        # Machine incidents frame
        machine_incidents_frame = ttk.Frame(incident_summary_frame)
        machine_incidents_frame.rowconfigure(0, weight=1)
        machine_incidents_frame.rowconfigure(1, weight=1)
        machine_incidents_frame.rowconfigure(2, weight=1)
        machine_incidents_frame.rowconfigure(3, weight=1)
        machine_incidents_frame.rowconfigure(4, weight=1)
        machine_incidents_frame.columnconfigure(0, weight=2)
        machine_incidents_frame.columnconfigure(1, weight=1)

        ttk.Label(machine_incidents_frame, text="MACHINE INCIDENTS",
                  style=self.SUBHEADING_STYLE_CLASS)\
            .grid(row=0, column=0, columnspan=2)

        ttk.Label(machine_incidents_frame, text="Machine Stopped")\
            .grid(row=1, column=0, sticky=W, padx=20, pady=6)
        entry1 = ttk.Entry(machine_incidents_frame)
        entry1.insert(0, "4")
        entry1.configure(state=DISABLED, width=3)
        entry1.grid(row=1, column=2, sticky=E, padx=5, pady=6)

        ttk.Label(machine_incidents_frame, text="Machine Alarm Sounded")\
            .grid(row=2, column=0, sticky=W, padx=20, pady=6)
        entry2 = ttk.Entry(machine_incidents_frame)
        entry2.insert(0, "0")
        entry2.configure(state=DISABLED, width=3)
        entry2.grid(row=2, column=2, sticky=E, padx=5, pady=6)

        ttk.Label(machine_incidents_frame, text="Poka-Yoke Malfunctioning")\
            .grid(row=3, column=0, sticky=W, padx=20, pady=6)
        entry3 = ttk.Entry(machine_incidents_frame)
        entry3.insert(0, "1")
        entry3.configure(state=DISABLED, width=3)
        entry3.grid(row=3, column=2, sticky=E, padx=5, pady=6)

        ttk.Label(machine_incidents_frame, text="Machine Stopped")\
            .grid(row=4, column=0, sticky=W, padx=20, pady=6)
        entry4 = ttk.Entry(machine_incidents_frame)
        entry4.insert(0, "0")
        entry4.configure(state=DISABLED, width=3)
        entry4.grid(row=4, column=2, sticky=E, padx=5, pady=6)

        machine_incidents_frame.grid(
            row=0, column=0, sticky=(N, E, S), ipadx=30)

        # Part incidents frame
        part_incidents_frame = ttk.Frame(incident_summary_frame)
        part_incidents_frame.rowconfigure(0, weight=1)
        part_incidents_frame.rowconfigure(1, weight=1)
        part_incidents_frame.rowconfigure(2, weight=1)
        part_incidents_frame.columnconfigure(0, weight=1)
        part_incidents_frame.columnconfigure(1, weight=2)

        ttk.Label(part_incidents_frame, text="PART INCIDENTS",
                  style=self.SUBHEADING_STYLE_CLASS)\
            .grid(row=0, column=0, columnspan=2, sticky=N)

        entry5 = ttk.Entry(part_incidents_frame)
        entry5.insert(0, "3")
        entry5.configure(state=DISABLED, width=3)
        entry5.grid(row=1, column=0, padx=5, pady=6)
        ttk.Label(part_incidents_frame, text="NOK Parts")\
            .grid(row=1, column=1, padx=20, pady=6, sticky=W)

        entry6 = ttk.Entry(part_incidents_frame)
        entry6.insert(0, "6")
        entry6.configure(state=DISABLED, width=3)
        entry6.grid(row=2, column=0, padx=5, pady=6)
        ttk.Label(part_incidents_frame, text="OK Parts with Quality Deviation")\
            .grid(row=2, column=1, padx=20, pady=6, sticky=W)

        part_incidents_frame.grid(row=0, column=2, sticky=(N, W, S))

    def on_homepage_click(self):
        self.parent.show_page()

    def on_incident_list_click(self):
        pass
