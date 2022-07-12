def random_init(board:boardtype) -> None:
    for i in range(len(board)):
        for j in range(len(board[0])):
            a = random()
            board[i][j].marked = False
            if a < 0.5:
                board[i][j].value = 0
            else:
                board[i][j].value = 1

def update_field(f: tkinter.Canvas) -> None:
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j].value == 1:
                field.create_rectangle(i*21, j*21, i*21 + 20,j*21 + 20, fill='chartreuse2')
            else:
                field.create_rectangle(i*21, j*21, i*21 + 20, j*21+20, fill='brown4')

def calculate_neighbours(board: list[list[Cell]], row: int, col: int):
    neighbours = 0
    for i in range(row-1,row+2):
        for j in range(col-1, col+2):
            if i >= 0 and j >= 0 and i < len(board) and j < len(board[0]):
                neighbours += board[i][j].value 
    neighbours -= board[row][col].value 
    return neighbours
    
def check_all_cells(board: list[list[Cell]]) -> None:
    for row in range(len(board)):
        for col in range(len(board)):
            number_of_neighbours = calculate_neighbours(board, row, col)
            if board[row][col].value == 1:
                if number_of_neighbours > 3:
                    board[row][col].marked = False
                if number_of_neighbours < 2:
                    board[row][col].marked = False
                if number_of_neighbours == 2 or number_of_neighbours ==3:
                    board[row][col].marked = True
                elif board[row][col].value == 0:
                    if number_of_neighbours == 3:
                        board[row][col].marked = True 
                    else:board[row][col].marked = False

def update_board(board: list[list[Cell]]) -> None:
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col].marked == True:
                board[row][col].value = 1
            else:
                board[row][col].value = 0 

def run_and_canvas(board: list[list[Cell]], f: tkinter.Canvas) -> None:
    check_all_cells(board)
    update_board(board)
    update_field(f)
