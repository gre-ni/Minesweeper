from tkinter import Label

class Cell:
    def __init__(self, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None

    # Defining this so that I don't raise errors with label-interactive behavior
    def left_click_action(self, event=None):
        
        # Implementing pressed look on clicking:
        if self.cell_btn_object: # Ensures I don't accidentally call None object
            self.cell_btn_object.config(relief="sunken")
            # Returning it back to raised:
            self.cell_btn_object.after(100, lambda: self.cell_btn_object.config(relief="raised"))

    def create_btn_object(self, location):
        lbl = Label( # Need to have label instead of button because of Mac behaviour
            location,
            text="Text",
            bg="#AAAAAA",
            width=4,
            height=2,
            relief="raised",
            borderwidth=2
        )
        lbl.bind("<Button-1>", lambda e: self.left_click_action())
        # .bind allows labels listen to events
        # <Button-1> == event which represents left mouse click

        self.cell_btn_object = lbl