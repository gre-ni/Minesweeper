from cell import Cell
import settings
# GUI library -> comes with Python:
from tkinter import *
import utils

# "root" -> naming convention for tkinter projects:
root = Tk() # Instantiation of a window

# Window settings:
root.geometry(f"{settings.WIDTH}x{settings.HEIGHT}")
root.resizable(False, False)
root.configure(bg="#2C2C2C")
root.title("Minesweeper game")

# Frames:
top_frame = Frame(
    root, # Location
    bg="#202020",
    width=utils.width_prct(100),
    height=utils.height_prct(25),
    highlightbackground="#525252",
    highlightthickness=1
)
top_frame.place(x=0,y=0)

# Frames:
left_frame = Frame(
    root, # Location
    bg="#202020",
    width=utils.width_prct(25),
    height=settings.HEIGHT-utils.height_prct(25),
    highlightbackground="#525252",
    highlightthickness=1
)
left_frame.place(x=0,y=utils.height_prct(25)-1) # -1 For border overlap

# Frames:
centre_frame = Frame(
    root, # Location
    bg="#2C2C2C",
    width=utils.width_prct(75),
    height=settings.HEIGHT-utils.height_prct(25),
    highlightbackground="#525252",
    highlightthickness=1
)
centre_frame.place(x=utils.width_prct(25)-1,y=utils.height_prct(25)-1) # -1 For border overlap

# Instantiate a grid of cell objects:
for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_object(centre_frame)
        c.cell_btn_object.grid(
            column=x, row=y
            )

# Call label object, pass in location:
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(
    x=10, y=10
)

# Place mines to random locations:
Cell.randomise_mines()


# Run the window:
root.mainloop() # It will run until I close it
