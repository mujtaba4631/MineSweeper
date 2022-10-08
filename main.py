from tkinter import *
import tkinter
from tkinter.font import BOLD
from cell import Cell
import settings
import utils


root = Tk()
# Override the settings of the window
root.configure(bg="#f7ab07")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title("Minesweeper Game")
root.resizable(False, False)
photo = PhotoImage(file='MINE SWEEPER.png')

top_frame = Frame(
    root,
    bg='black',
    width=settings.WIDTH,
    height=utils.height_prct(25)
)
top_frame.place(x=0, y=0)

game_title = Label(
    top_frame,
    bg='black',
    fg='white',
    image=photo,
    font=('Comic Sans MS', 48, BOLD),  
)

game_title.place(
    x=0, y=0
)

left_frame = Frame(
    root,
    bg= '#f7ab07',
    width=utils.width_prct(25),
    height=utils.height_prct(75)
)
left_frame.place(x=10, y=utils.height_prct(35))

center_frame = Frame(
    root,
    bg='black',
    width=utils.width_prct(75),
    height=utils.height_prct(75)
)
center_frame.place(
    x=utils.width_prct(30),
    y=utils.height_prct(30),
)

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=x, row=y
        )
# Call the label from the Cell class
Cell.create_cell_count_label(left_frame)
Cell.create_mine_count_label(left_frame)
Cell.cell_count_label_object.place(
    x=0, y=50
)
Cell.randomize_mines()


# Run the window
root.mainloop()
