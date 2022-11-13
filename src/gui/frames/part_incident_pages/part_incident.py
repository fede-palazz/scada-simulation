from tkinter import *
from tkinter import ttk
from gui.frames.part_incident_pages.defect_type import DefectTypeFrame


class PartFrame(ttk.Frame):
    def __init__(self, container, style, style_class=""):
        super().__init__(container, style=style_class)

        # Constants
        self.HEADING_TEXT = "Part Incident"
        self.HEADING_STYLE_CLASS = "Heading.Part.TLabel"
        self.BTN_STYLE_CLASS = "Part.TButton"
        self.DEFECT_TYPE_STYLE_CLASS = "DefectType.Part.TFrame"
        self.DEFECT_LOCATION_STYLE_CLASS = "DefectLoc.Part.TFrame"
        self.NAVBAR_STYLE_CLASS = "Navbar.Part.TFrame"

        # defect_name: has_location
        self.OK_PART_DEFECTS = {
            "slight burrs": True,
            "slight marbling": True,
            "hotter than usual": False,
            "color nok": True,
            "oil gas": True,
            "mark": True,
            "surface bubble": True,
            "slight burrs": False,
            "test1": True,
            "test2": True,
            "test3": False,
            "test4": True,
        }
        self.NOK_PART_DEFECTS = {
            "burrs": True,
            "marbling": True,
            # "color nok": True,
            # "oil gas": True,
            # "mark": True,
            # "deformation": True,
            # "surface bubble": True,
            # "lack material": True,
            # "short piece": True,
        }

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
            "font": ("Arial", 18, "bold"),
            "background": parent_bg_color,
        }
        defect_type_options = {
            "background": parent_bg_color
        }
        defect_location_options = {
            "background": parent_bg_color
        }
        navbar_options = {
            "background": parent_bg_color,
        }
        btn_options = {
            "font": ("Arial", 14)
        }
        self.style.configure(self.HEADING_STYLE_CLASS, **heading_options)
        self.style.configure(self.BTN_STYLE_CLASS, **btn_options)
        self.style.configure(self.DEFECT_TYPE_STYLE_CLASS,
                             **defect_type_options)
        self.style.configure(self.NAVBAR_STYLE_CLASS, **navbar_options)

    def __create_widgets(self):
        self.heading_lbl = ttk.Label(
            self, text=self.HEADING_TEXT, style=self.HEADING_STYLE_CLASS)
        # Buttons
        self.ok_part_btn = ttk.Button(self,
                                      text="OK PART",
                                      style=self.BTN_STYLE_CLASS,
                                           command=lambda: self.on_okpart_click())
        self.nok_part_btn = ttk.Button(self,
                                       text="NOT OK PART",
                                       style=self.BTN_STYLE_CLASS,
                                       command=lambda: self.on_nokpart_click())

        # Sub-pages
        self.ok_part_frame = DefectTypeFrame(
            self, self.style, is_ok_part=True,
            defects=self.OK_PART_DEFECTS,
            style_class=self.DEFECT_TYPE_STYLE_CLASS)
        self.nok_part_frame = DefectTypeFrame(
            self, self.style, is_ok_part=False,
            defects=self.NOK_PART_DEFECTS,
            style_class=self.DEFECT_TYPE_STYLE_CLASS)

        # Bottom Navbar
        self.navbar = ttk.Frame(self, style=self.NAVBAR_STYLE_CLASS)
        self.home_btn = ttk.Button(
            self.navbar, text="HOME", style=self.BTN_STYLE_CLASS, command=lambda: self.show_homepage())
        self.back_btn = ttk.Button(
            self.navbar, text="BACK", style=self.BTN_STYLE_CLASS, command=lambda: self.show_homepage())

    def __render_widgets(self):
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)  # Heading label
        self.rowconfigure(1, weight=2)  # Ok part btn
        self.rowconfigure(2, weight=2)  # Nok part btn
        self.rowconfigure(3, weight=1)  # Blank space
        self.rowconfigure(4, weight=1)  # Bottom navbar
        self.rowconfigure(5, weight=1)  # Blank space

        paddings_btn = {"padx": 20, "ipady": 10, "ipadx": 10}
        # Heading
        self.heading_lbl.grid(row=0, column=0)
        # Buttons
        self.ok_part_btn.grid(row=1, column=0, **paddings_btn)
        self.nok_part_btn.grid(row=2, column=0, **paddings_btn)
        # Navbar
        self.navbar.grid(row=4, column=0)
        paddings_btn = {"padx": 20, "ipady": 10, "ipadx": 10, "pady": 0}
        self.home_btn.pack(side=LEFT, **paddings_btn)
        self.back_btn.pack(side=RIGHT, **paddings_btn)

    def show_homepage(self):
        # Destroy sub-frames
        self.ok_part_frame.grid_forget()
        self.nok_part_frame.grid_forget()
        self.parent.show_page()

    def on_okpart_click(self):
        """ Show ok_part frame """
        self.ok_part_frame.grid(row=1, column=0,
                                sticky=(N, S, E, W),
                                rowspan=3)
        # Change behaviour of Back button
        self.back_btn.configure(command=self.hide_children)
        self.ok_part_frame.tkraise()

    def on_nokpart_click(self):
        """ Show nok_part frame """
        self.nok_part_frame.grid(row=1, column=0,
                                 sticky=(N, S, E, W),
                                 rowspan=3)
        # Change behaviour of Back button
        self.back_btn.configure(command=self.hide_children)
        self.nok_part_frame.tkraise()

    def hide_children(self):
        self.ok_part_frame.grid_forget()
        self.nok_part_frame.grid_forget()
        # Restore normal Back button behaviour
        self.back_btn.configure(command=self.show_homepage)
