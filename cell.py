from tkinter import Label
import random
import settings

class Cell:
    all = [] # This list will populate as all objects get instantiated, as append is part of init
    cell_count = settings.GRID_SIZE ** 2
    cell_count_label_object = None
    
    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.is_opened = False
        self.is_mine_candidate = False
        self.x = x
        self.y = y
        self.cell_btn_object = None
        
        Cell.all.append(self)


    def create_btn_object(self, location):
        lbl = Label( # Need to have label instead of button because of Mac behaviour
            location,
            bg="#AAAAAA",
            width=4,
            height=2,
            relief="raised",
            borderwidth=2,
            # text=f"{self.x}, {self.y}"
        )
        # .bind allows labels listen to events
        # <Button-1> == event which represents left mouse click
        lbl.bind("<Button-1>", self.left_click_actions)
        lbl.bind("<Button-2>", self.right_click_actions)
        
        self.cell_btn_object = lbl
    
        
    # In tkinter event functions need to have both of these arguments:
    def left_click_actions(self, event):       
        if self.is_mine:
            self.show_mine()
        else:
            # Automatically uncover empty areas:
            if self.surrounding_cells_amount == 0:
                for cell_obj in self.surrounding_cells:
                    cell_obj.show_cell()
            self.show_cell()


    def right_click_actions(self, event):
        # Aesthetic:
        if self.cell_btn_object: # Ensures I don't accidentally call None object
            self.cell_btn_object.config(relief="sunken")
            # Returning it back to unpressed:
            self.cell_btn_object.after(200, lambda: self.cell_btn_object.config(relief="raised"))
        
        if not self.is_mine_candidate:
            self.cell_btn_object.configure(bg="#D6D6D6", text="🚩")
            self.is_mine_candidate = True
        else:
            self.cell_btn_object.configure(bg="#AAAAAA", text="")
            self.is_mine_candidate = False
    
    
    def show_mine(self):
        # TODO: Logic to interrupt the game and display a message that player lost.
        # Temporary solution while working:
        self.cell_btn_object.configure(bg="#E82C2C")
    
    
    @property # Converts to read-only kind of attribute
    def surrounding_cells(self):
        # Using linear search instead of indexing -> no risk of index error
        # Corner/edge cells just have None objects in their list
        cells = [
            # Row above
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            # Same row
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y),
            # Row below
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y + 1),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
        ]
        
        # Clean up None values by using list comprehension:
        cells = [cell for cell in cells if cell is not None]
        return cells
   
   
    @property
    def surrounding_cells_amount(self):
        counter = 0
        for cell in self.surrounding_cells:
            if cell.is_mine:
                counter += 1
        
        return counter
   
    
    def show_cell(self):
        if not self.is_opened: # Only count each shown cell once
            Cell.cell_count -= 1
            self.cell_btn_object.configure(text=f"{self.surrounding_cells_amount}", relief="sunken")
            if Cell.cell_count_label_object: # Check first that label is initialised
                Cell.cell_count_label_object.configure(text=f"Cells left: {Cell.cell_count}") # Refresh info

        self.is_opened = True


    def get_cell_by_axis(self, x, y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell
    
    
    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(
            location, 
            bg="#2C2C2C",
            text=f"Cells left: {Cell.cell_count}",
            fg="white",
            font=("Helvetica", 22),
            width=12,
            height=2
        )
        Cell.cell_count_label_object = lbl


    @staticmethod
    def randomise_mines():
        picked_cells = random.sample(
            Cell.all, settings.MINES_COUNT)
        for picked_cell in picked_cells:
            picked_cell.is_mine = True
    
    
    # For debugging:
    def __repr__(self):
        return f"Cell({self.x}, {self.y})"