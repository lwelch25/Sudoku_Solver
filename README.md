# Sudoku_Solver
This is a Python program that solves Sudoku puzzles by recursively trying different numbers for each empty cell until a solution is found. The program uses a backtracking algorithm to solve the puzzle.

Usage
To use this program, you need to provide a Sudoku puzzle as a grid of numbers. You can change the grid variable at the beginning of the program to input a new Sudoku problem.

```# CHANGE grid every new sudoku problem
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
```
Once you have provided the Sudoku problem, run the program and a GUI window will open displaying the Sudoku board. Click the "Solve" button to solve the puzzle. The program will fill in the empty cells with the correct numbers and update the display on the GUI.

Functions
The program has three main functions:

check_valid_number_placement(row, column, number): This function checks if the given number can be placed in the given row and column of the grid. It returns True if the number can be placed, False otherwise.

solve(): This function solves the Sudoku puzzle by backtracking and recursively trying different numbers for each empty cell until a solution is found. It calls the check_valid_number_placement() function to check if a number can be placed in a cell. When a solution is found, it calls the update_grid_display() function to update the display of the grid.

update_grid_display(): This function updates the display of the grid on the GUI by iterating over each cell in the grid, getting the value from the grid, and inserting it into the corresponding entry in the GUI.

GUI
The program uses the tkinter module to create a GUI for the Sudoku board. It creates a 9x9 grid of Entry widgets to display the Sudoku board, and sets the initial values of the Entry widgets to the corresponding values in the grid. The program also creates a "Solve" button that calls the solve() function when clicked.

Note
Remember to change the grid variable to input a new Sudoku problem every time you run the program.
