from tkinter import *
# Library for UI -> comes with Python

# "root" is naming convention for tkinter projects:
root = Tk() # Instantiation of a window

# Window settings:
root.geometry("1440x720")
root.resizable(False, False)
root.configure(bg="#2C2C2C")
root.title("Minesweeper game")

# Frames:
top_frame = Frame(
    root, # Location
    bg="#202020",
    width=1440,
    height=180
)
top_frame.place(x=0,y=0)

# Run the window:
root.mainloop() # It will run until I close it
