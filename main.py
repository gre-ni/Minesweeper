from cell import Cell
import settings
from tkinter import *
import utils
# Library for UI -> comes with Python

# "root" is naming convention for tkinter projects:
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
# I want the pixel line of top and left frame to overlap
left_frame.place(x=0,y=utils.height_prct(25)-1) 

# Frames:
centre_frame = Frame(
    root, # Location
    bg="#2C2C2C",
    width=utils.width_prct(75),
    height=settings.HEIGHT-utils.height_prct(25),
    highlightbackground="#525252",
    highlightthickness=1
)
# I want the pixel line of top and left frame to overlap
centre_frame.place(x=utils.width_prct(25)-1,y=utils.height_prct(25)-1) 

# Using buttons for cells
c1 = Cell()
c1.create_btn_object(centre_frame)
c1.cell_btn_object.place(x=0, y=0)

# Run the window:
root.mainloop() # It will run until I close it
