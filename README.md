# GUI-SUDOKU-Game-Solver

## Introduction

This project is a fully fledged Sudoku application built with Python, featuring a graphical user interface (GUI) and a solver. The user is presented with a randomized solvable Sudoku board, and can insert "sketched-in" numbers into the fields without restriction. However, to definitively place a number, the program checks if the number leads to a valid solution.

## Features

* Randomized and solvable Sudoku board generation at runtime;
* Graphical user interface (GUI) using the Pygame library;
* "Sketching" mode for inserting temporary numbers;
* Real-time board validation for checking if a placed number is valid;
* Solver algorithm to solve given Sudoku board (or determine if is invalid);
* Timer for testing your performance on solving the board;
* Systems that keeps track of the wrong entries;
* Extended use of the core OOP principles;


## Installation 

1. Clone this repository: `git clone https://github.com/davidandw190/GUI-SUDOKU-Game-Solver.git`
2. Install the required libraries: `pip install pygame`
3. Run the game: `python GUI.py`


## Usage

Upon running the game, the user is presented with an at-runtime valid randomized Sudoku board. The user can click on any empty cell to select it, and then insert a number from 1 to 9. The number is first placed in the cell in a "Sketched-In" mode, or rather temporay mode, in which the program does not evaluate if the placed number is vaid and it. This sketching mode allows the user to insert numbers without committing to them.

To definitively place a number, the user can press the Enter key. The program will check if the board is still solvable with the new number, and if it is not, an X will appear on the bottom-left of the screen to showcase an unsuccessful answer. If the board is solvable, the number is placed in the cell.

Algorithmic Side
The solver algorithm is based on a backtracking algorithm that tries to fill each cell with a valid number. If it reaches a dead end where no valid number can be placed, it backtracks to the previous cell and tries a different number. This process is repeated until the entire board is filled.

The algorithm uses a recursive function to perform the backtracking, and also uses a few optimization techniques such as checking for valid numbers in each row, column, and 3x3 block before attempting to place a number.
