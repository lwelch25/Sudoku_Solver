import tkinter as tk

# Change grid every new sudoku problem
# Program new grid after bot it completed
grid = [[0,0,0,3,7,0,4,0,0],
        [0,8,0,4,2,9,0,0,0],
        [0,0,0,0,0,1,0,0,2],
        [0,0,6,0,0,0,0,7,5],
        [2,0,0,7,0,0,0,6,9],
        [0,5,0,0,0,0,2,4,8],
        [8,0,0,0,0,0,0,0,4],
        [0,3,1,9,0,0,6,0,0],
        [0,4,0,2,5,0,8,0,0]]

def check_valid_number_placement(row, column, number):
    global grid
    # If number is appearing in row = False
    for i in range(0,9):
        if grid[row][i] == number:
            return False
    # If number is appearing in column = False
    for i in range(0,9):
        if grid[i][column] == number:
            return False
    # If number is appearing in square = False
    x0 = (column // 3) * 3
    y0 = (row // 3) * 3
    for i in range(0,3):
        for j in range(0,3):
            if grid[y0+i][x0+j] == number:
                return False

    return True

def solve():
    global grid
    for row in range(0,9):
        for column in range(0,9):
            if grid[row][column] == 0:
                for number in range(1,10):
                    if check_valid_number_placement(row, column, number):
                        grid[row][column] = number
                        solve()
                        grid[row][column] = 0
                return 

    update_grid_display()

def update_grid_display():
    global grid
    for i in range(9):
        for j in range(9):
            cell = cells[i][j]
            value = grid[i][j]
            cell.config(state='normal')
            cell.delete(0, tk.END)
            cell.insert(0, value)
            cell.config(state='disabled')

# Sudoku Board
def create_sudoku_board():
    global grid
    global cells
    root = tk.Tk()
    root.title("Sudoku Solver")
    board_frame = tk.Frame(root)
    board_frame.pack()
    cells = []
    for i in range(9):
        row = []
        for j in range(9):
            cell_frame = tk.Frame(
                board_frame,
                highlightbackground="black",
                highlightthickness=1,
                width=30,
                height=30
            )
            cell_frame.grid(row=i, column=j)
            cell_entry = tk.Entry(cell_frame, justify='center', font=('Arial', 16), width=2)
            if grid[i][j] != 0:
                cell_entry.insert(0, grid[i][j])
                cell_entry.config(state='disabled')
            cell_entry.grid()
            row.append(cell_entry)
        cells.append(row)
    solve_button = tk.Button(root, text="Solve", command=solve)
    solve_button.pack()
    root.mainloop()

if __name__ == '__main__':
    create_sudoku_board()