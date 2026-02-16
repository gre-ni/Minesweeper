from cell import Cell
import settings
# GUI library -> comes with Python:
from tkinter import *
import utils


root = Tk() # Instantiation of a window

# Window settings:
root.geometry(f"{settings.WIDTH}x{settings.HEIGHT}")
root.resizable(False, False)
root.configure(bg=settings.BG_COLOUR)
root.title("Minesweeper game")


# Frames:

top_frame = Frame(
    root, # Location
    bg=settings.BG_COLOUR,
    width=utils.width_prct(100),
    height=utils.height_prct(10),
    highlightbackground=settings.LINE_COLOUR,
    highlightthickness=1
)
top_frame.place(x=0,y=0)


left_frame = Frame(
    root, # Location
    bg=settings.BG_COLOUR,
    width=utils.width_prct(25),
    height=settings.HEIGHT-utils.height_prct(10),
    highlightbackground=settings.LINE_COLOUR,
    highlightthickness=1
)
left_frame.place(x=0,y=utils.height_prct(10)-1) # -1 For border overlap


centre_frame = Frame(
    root, # Location
    bg=settings.BG_COLOUR,
    width=utils.width_prct(75),
    height=settings.HEIGHT-utils.height_prct(10),
    highlightbackground=settings.LINE_COLOUR,
    highlightthickness=1
)
centre_frame.place(x=utils.width_prct(25)-1,y=utils.height_prct(10)-1) # -1 For border overlap

# Instantiate a grid of cell objects:
for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_object(centre_frame)
        c.cell_btn_object.grid(
            column=x, row=y
            )

# Call label object for status display:
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(
    x=10, y=10
)

# Place mines to random locations:
Cell.randomise_mines()


# Run the window until closed:
root.mainloop()
