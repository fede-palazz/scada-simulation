from tkinter import *
from tkinter import ttk
from gui.header import HeaderFrame
from gui.homepage import HomeFrame
from gui.frames.summary import SummaryFrame
from gui.frames.part_incident import PartFrame
from gui.frames.machine_incident import MachineFrame
from gui.frames.last_reported import LastReportedFrame


class OperatorHMI(Tk):
    def __init__(self):
        super().__init__()

        # Constants
        self.ASSETS_PATH = "src/assets/"
        self.IMG_PATH = self.ASSETS_PATH + "imgs/machine.jpg"
        self.HEADER_STYLE_CLASS = "Header.TFrame"
        self.HOME_STYLE_CLASS = "Home.TFrame"
        self.SUMMARY_STYLE_CLASS = "Summary.TFrame"
        self.PART_STYLE_CLASS = "Part.TFrame"
        self.MACHINE_STYLE_CLASS = "Machine.TFrame"
        self.LAST_REPORTED_STYLE_CLASS = "LastReported.TFrame"

        # Window config
        self.title('Operator HMI')
        self.resizable(0, 0)
        self.geometry('750x850')

        # Global styling options
        self.style = ttk.Style(self)
        # Sub frames
        self._pages = {}

        # Initialise widgets
        self.__configure_style()
        self.__create_widgets()
        self.__render_widgets()

    def __configure_style(self):
        header_options = {
            "background": "grey",
        }
        home_options = {
            "background": "lightgrey"
        }
        self.style.configure(self.HEADER_STYLE_CLASS, **header_options)
        self.style.configure(self.HOME_STYLE_CLASS, **home_options)
        self.style.configure("Header.TLabel", foreground="white")

        self.style.configure(self.SUMMARY_STYLE_CLASS,
                             background="lightsalmon")
        self.style.configure(self.PART_STYLE_CLASS,
                             background="lightgreen")
        self.style.configure(self.MACHINE_STYLE_CLASS,
                             background="lightblue")
        self.style.configure(self.LAST_REPORTED_STYLE_CLASS,
                             background="lightyellow")

    def __create_widgets(self):
        # Header frame
        self.header_frame = HeaderFrame(
            self, self.style, self.HEADER_STYLE_CLASS)

        for frame in (HomeFrame,
                      SummaryFrame,
                      PartFrame,
                      MachineFrame,
                      LastReportedFrame):
            # Assign the class name
            page_name = frame.__name__
            # Create frame and set style
            # TODO: use a shared style for all the pages
            page = frame(self, self.style,
                         page_name.replace("Frame", ".TFrame"))
            # Add new page to the dict
            self._pages[page_name] = page

    def __render_widgets(self):
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=20)
        self.columnconfigure(0, weight=1)

        # Render header frame
        self.header_frame.grid(column=0, row=0, sticky=(N, W, E, S))
        # Render all the pages
        for page in self._pages.values():
            page.grid(row=1, column=0, sticky=(N, S, E, W))
        # Display the home frame
        # TODO: Show homepage
        self.show_page("MachineFrame")

    def show_page(self, page_name=""):
        '''Show a frame for the given page name'''
        if page_name in self._pages:
            self._pages[page_name].tkraise()
        elif page_name == "":
            self._pages["HomeFrame"].tkraise()
        else:
            raise Exception("Requested page not found")
