from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class MachineFrame(ttk.Frame):
    def __init__(self, container, style, style_class=""):
        super().__init__(container, style=style_class)

        # Constants
        self.HEADING_TEXT = "Machine Incident"
        self.INCIDENT_TYPES_NUM = 4  # Incident types number
        self.HEADING_STYLE_CLASS = "Heading.Machine.TLabel"
        self.CBX_STYLE_CLASS = "Machine.TCheckbutton"
        self.NAVBAR_STYLE_CLASS = "Navbar.Machine.TFrame"
        self.NAVBAR_BTN_STYLE_CLASS = "Navbar.Machine.TButton"

        self.style = style
        self.style_class = style_class
        self.parent = container

        # Checkbox selection
        self._cbx_sel = []
        for _ in range(self.INCIDENT_TYPES_NUM):
            var = StringVar()
            var.set(0)  # Checkboxes initially unchecked
            self._cbx_sel.append(var)

        # Initialise widgets
        self.__configure_style()
        self.__create_widgets()
        self.__render_widgets()

    def __configure_style(self):
        # Parent bg color
        parent_bg_color = self.style.lookup(
            self.style_class, "background")
        heading_options = {
            "font": ("Arial", 18, "bold"),
            "background": parent_bg_color,
        }
        cbx_options = {
            "background": parent_bg_color,
            "font": ("Arial", 16),
        }
        navbar_options = {
            "background": parent_bg_color,
        }
        navbar_btn_options = {
            "font": ("Arial", 14)
        }
        self.style.configure(self.HEADING_STYLE_CLASS,
                             **heading_options)
        self.style.configure(self.CBX_STYLE_CLASS,
                             **cbx_options)
        self.style.configure(self.NAVBAR_STYLE_CLASS,
                             **navbar_options)
        self.style.configure(self.NAVBAR_BTN_STYLE_CLASS,
                             **navbar_btn_options)

    def __create_widgets(self):
        self.heading_lbl = ttk.Label(
            self, text=self.HEADING_TEXT, style=self.HEADING_STYLE_CLASS)
        # Checkboxes
        self.stopped_cbx = ttk.Checkbutton(
            self,
            text="Machine stopped",
            variable=self._cbx_sel[0],
            style=self.CBX_STYLE_CLASS)
        self.alarm_cbx = ttk.Checkbutton(
            self,
            text="Machine alarm sounded",
            variable=self._cbx_sel[1],
            style=self.CBX_STYLE_CLASS)
        self.pokayoke_cbx = ttk.Checkbutton(
            self,
            text="Poka-yoke malfunctioning",
            variable=self._cbx_sel[2],
            style=self.CBX_STYLE_CLASS)
        self.noise_cbx = ttk.Checkbutton(
            self,
            text="Abnormal noise from the machine",
            variable=self._cbx_sel[3],
            style=self.CBX_STYLE_CLASS)
        # Bottom Navbar
        self.navbar = ttk.Frame(self, style=self.NAVBAR_STYLE_CLASS)
        self.back_btn = ttk.Button(
            self.navbar, text="BACK", style=self.NAVBAR_BTN_STYLE_CLASS, command=lambda: self.on_back_click())
        self.report_btn = ttk.Button(
            self.navbar, text="REPORT", style=self.NAVBAR_BTN_STYLE_CLASS, command=lambda: self.on_report_click())

    def __render_widgets(self):
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)
        self.rowconfigure(6, weight=1)
        self.rowconfigure(7, weight=1)

        paddings = {"padx": 150}
        # Heading
        self.heading_lbl.grid(row=0, column=0)
        # Checkboxes
        self.stopped_cbx.grid(row=1, column=0, sticky=(W), **paddings)
        self.alarm_cbx.grid(row=2, column=0, sticky=(W), **paddings)
        self.pokayoke_cbx.grid(row=3, column=0, sticky=(W), **paddings)
        self.noise_cbx.grid(row=4, column=0, sticky=(W), **paddings)
        # Navbar
        self.navbar.grid(row=6, column=0)
        paddings_btn = {"padx": 20, "ipady": 10, "ipadx": 10}
        self.back_btn.pack(side=LEFT, **paddings_btn)
        self.report_btn.pack(side=RIGHT, **paddings_btn)

    def on_check(self):
        # TODO: Enable report button if at least one cbx is checked
        pass

    def on_back_click(self):
        """ Reset frame state and show homepage """
        self.reset_state()
        self.parent.show_page()

    def on_report_click(self):
        # TODO: Implement machine incident report functionality
        # Show report confirmation message
        messagebox.showinfo(title="Report Status",
                            message="Machine incident successfully reported!")
        # TODO: Handle report errors
        self.reset_state()
        self.parent.show_page()

    def reset_state(self):
        """ Reset checkbox values """
        for value in self._cbx_sel:
            value.set(0)
