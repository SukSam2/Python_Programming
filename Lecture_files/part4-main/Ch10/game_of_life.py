from dataclasses import dataclass
import tkinter
from random import random
import sys

if sys.version_info.major == 3 and sys.version_info.minor >= 9:
    listtype = list
else:
    from typing import List
    listtype = List

@dataclass
class Cell:
    value: int
    marked: bool = False
    
boardtype = listtype[listtype[Cell]]


board = list()
for i in range(10):
    board.append(list())
    for j in range(10):
        board[-1].append(Cell((i+j) % 2))


root = tkinter.Tk()
field = tkinter.Canvas(root, width=220,height=220)
field.pack()
next_button = tkinter.Button(root, text="Next Iteration", command=lambda : run_and_canvas(board, field))
next_button.pack()
init_button = tkinter.Button(root, text="New Initialization", command=lambda : random_init_tk(board, field))
init_button.pack()
tkinter.mainloop()

for i in range(len(board)):
    for j in range(len(board)):
        if board[i][j].value == 1:
            field.create_rectangle(i*21, j*21, i*21 + 20,j*21 + 20, fill='chartreuse2')
        else:
            field.create_rectangle(i*21, j*21, i*21 + 20, j*21+20, fill='brown4')