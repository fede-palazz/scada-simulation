from tkinter import *
from tkinter import ttk


class DefectTypeFrame(ttk.Frame):
    def __init__(self, container,
                 style, is_ok_part,
                 defects, style_class=""):
        super().__init__(container, style=style_class)

        # Constants
        # TODO: Change heading text
        self.BTN_STYLE_CLASS = "DefectType.Part.TButton"
        self.OFFSET = 6  # Display six buttons per view

        self.style = style
        self.style_class = style_class
        self.parent = container

        self.is_ok_part = is_ok_part
        # Dict of possibile part defects
        self.defects = defects
        self.btn_list = []  # Buttons list
        self.current_page = 0   # Current page view

        # Initialise widgets
        self.__configure_style()
        self.__create_widgets()
        self.__render_widgets()

    def __configure_style(self):
        parent_bg_color = self.style.lookup(
            self.style_class, "background")
        btn_options = {
            "font": ("Arial", 14),
        }
        self.style.configure(self.BTN_STYLE_CLASS, **btn_options)

    def __create_widgets(self):
        # Create buttons list
        for defect in self.defects:
            self.btn_list.append(ttk.Button(self, text=defect,
                                            style=self.BTN_STYLE_CLASS))
        # Navigation buttons
        self.next_page_btn = ttk.Button(self, text="-->",
                                        command=lambda: self.__on_next_page_click())
        self.previous_page_btn = ttk.Button(self, text="<--",
                                            command=lambda: self.__on_previous_page_click())

    def __render_widgets(self):
        self.columnconfigure(0, weight=1)   # Previous page btn
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)   # Next page btn
        self.rowconfigure(0, weight=1)  # Btn 1,2
        self.rowconfigure(1, weight=1)  # Btn 3,4
        self.rowconfigure(2, weight=1)  # Btn 5,6

        # Display defect type buttons
        self.render_buttons()
        # Render navigation buttons
        if len(self.btn_list) > self.OFFSET:
            self.previous_page_btn.grid(row=1, column=0)
            self.next_page_btn.grid(row=1, column=3)
            self.update_nav_state()

    def render_buttons(self):
        """ Render buttons based on current displayed page """
        # Remove all the buttons from the view
        self.clear_view()
        # Render desidered buttons
        i = self.OFFSET*self.current_page   # Starting index
        while i < min(self.OFFSET*(1+self.current_page),
                      len(self.btn_list)):
            btn = self.btn_list[i]  # Get the button
            btn.grid(row=int((i % self.OFFSET)/2),
                     column=((i % self.OFFSET) % 2)+1,
                     ipadx=10, ipady=5)
            i += 1

    def clear_view(self):
        """ Remove all the rendered buttons """
        for btn in self.btn_list:
            btn.grid_forget()

    def __on_next_page_click(self):
        # Increase current page counter
        self.current_page += 1
        # Update view
        self.render_buttons()
        self.update_nav_state()

    def __on_previous_page_click(self):
        # Decrease current page counter
        self.current_page -= 1
        # Update view
        self.render_buttons()
        self.update_nav_state()

    def has_next_page(self):
        """ Return whether there are other pages after the current one """
        # Total number of pages to scroll
        total_pages = int(len(self.btn_list)/self.OFFSET) + 1
        # Check for next page
        return self.current_page+1 < total_pages

    def has_previous_page(self):
        """ Return whether there are other pages before the current one """
        return self.current_page > 0

    def update_nav_state(self):
        """ Enable or disable navigation buttons based on current page """
        if self.has_next_page():
            self.next_page_btn["state"] = "normal"
        else:
            self.next_page_btn["state"] = "disabled"

        if self.has_previous_page():
            self.previous_page_btn["state"] = "normal"
        else:
            self.previous_page_btn["state"] = "disabled"

    def show_homepage(self):
        self.parent.hide_children()

    def has_location(self, defect_name):
        """ Check whether a type of defect has a specific location """
        if defect_name in self.defects:
            return self.defects.get(defect_name)
        raise Exception(defect_name + " defect not found inside dictionary")
