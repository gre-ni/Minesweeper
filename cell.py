from tkinter import Label
import random
import settings

class Cell:
    all = [] # This list will populate as all objects get instantiated, as append is part of init
    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.x = x
        self.y = y
        self.cell_btn_object = None
        
        Cell.all.append(self)


    def create_btn_object(self, location):
        lbl = Label( # Need to have label instead of button because of Mac behaviour
            location,
            text=f"{self.x}:{self.y}",
            bg="#AAAAAA",
            width=12,
            height=4,
            relief="raised",
            borderwidth=2
        )
        # .bind allows labels listen to events
        # <Button-1> == event which represents left mouse click
        lbl.bind("<Button-1>", self.left_click_actions)
        lbl.bind("<Button-2>", self.right_click_actions)
        
        self.cell_btn_object = lbl
        
        
    # In tkinter event functions need to have both of these arguments:
    def left_click_actions(self, event):       
         
        # Aesthetic
        if self.cell_btn_object: # Ensures I don't accidentally call None object
            self.cell_btn_object.config(relief="sunken")
            # Returning it back to unpressed:
            self.cell_btn_object.after(200, lambda: self.cell_btn_object.config(relief="raised"))
        
        # Function:
        print("I am left clicked!")


    def right_click_actions(self, event):
        
        # Aesthetic:
        if self.cell_btn_object: # Ensures I don't accidentally call None object
            self.cell_btn_object.config(relief="sunken")
            # Returning it back to unpressed:
            # self.cell_btn_object.after(200, lambda: self.cell_btn_object.config(relief="raised"))
        
        # Function:
        print("I am right clicked!")


    @staticmethod
    def randomise_mines():
        picked_cells = random.sample(
            Cell.all, settings.MINES_COUNT)
        for picked_cell in picked_cells:
            picked_cell.is_mine = True
    
    def __repr__(self):
        return f"Cell({self.x}, {self.y})"