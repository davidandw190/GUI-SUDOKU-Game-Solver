import pygame
from solver import pick_board, build_board, generate_board, solve, valid, find_empty
import time


pygame.font.init()

# Empty 9x9 board for construction of the randomised solvable starting board
default_board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]



class Cube:
    """
    Represents a cell in the Sudoku board.
    """
    rows = 9
    cols = 9

    def __init__(self, value, row, col, width, height):
        """
        Initializes a Cube object with the given value, row, column, width, and height.
        """
        self.value = value
        self.temp = 0
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.selected = False

    def draw(self, win):
        """
        Draws the cube on the given window.
        """
        font = pygame.font.SysFont("comiscsns", 40)

        gap = self.width / 9
        x = self.col * gap
        y = self.row * gap

        # Draws temporary value
        if self.temp != 0 and self.value == 0:
            text = font.render(str(self.temp), True, (128, 128, 128))
            win.blit(text, (x + 5, y + 5))
        # Draws permanent value
        elif not (self.value == 0):
            text = font.render(str(self.value), True, (0, 0, 0))
            win.blit(text, (x + (gap / 2 - text.get_width() / 2), y + (gap / 2 - text.get_height() / 2)))

        # Highlights selected cube
        if self.selected:
            pygame.draw.rect(win, (255, 0, 0), (x, y, gap, gap), 3)

    def set(self, val):
        """
        Sets the value of the cube to the given value.
        """
        self.value = val

    def set_temp(self, val):
        """
        Sets the temporary value of the cube to the given value.
        """
        self.temp = val


class Grid:
    board = default_board

    def __init__(self, rows, cols, width, height):
        self.rows = rows
        self.cols = cols
        self.cubes = [[Cube(self.board[i][j], i, j, width, height) for j in range(cols)] for i in range(rows)]
        self.width = width
        self.height = height
        self.model = None
        self.selected = None

    def update_model(self):
        """
        Updates the game board model.
        """
        self.model = [[self.cubes[i][j].value for j in range(self.cols)] for i in range(self.rows)]

    def place(self, val):
        """
        Places a value in the currently selected square if it is valid.

        """
        row, col = self.selected
        if self.cubes[row][col].value == 0:
            self.cubes[row][col].set(val)
            self.update_model()

            if valid(self.model, val, (row, col)) and solve(self.model):
                return True
            else:
                self.cubes[row][col].set(0)
                self.cubes[row][col].set_temp(0)
                return False

    def sketch(self, val):
        """
        Sketches a value in the currently selected square.
        """
        row, col = self.selected
        self.cubes[row][col].set_temp(val)

    def draw(self, win):
        """
        Draws the game board on the screen.
        """
        gap = self.width / 9

        for i in range(self.rows + 1):
            if i % 3 == 0 and i != 0:
                if i != self.rows:
                    thickness = 4
            else:
                thickness = 1

            pygame.draw.line(win, (0, 0, 0), (0, i * gap), (self.width, i*gap), thickness)
            pygame.draw.line(win, (0, 0, 0), (i * gap, 0), (i * gap, self.height), thickness)

        # Draw Cubes
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].draw(win)

    def select(self, row, col):
        """
        Selects a square on the Sudoku board
        """
        # Reset all other selected to False
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].selected = False

        # Selects and updates selected
        self.cubes[row][col].selected = True
        self.selected = (row, col)

    def clear(self):
        """
        Clears the value in the currently selected square.
        """
        row, col = self.selected
        if self.cubes[row][col].value == 0:
            self.cubes[row][col].set_temp = 0

    def click(self, pos):
        """
        Handles the logic when a user clicks a cell in the Sudoku grid.
        """
        if pos[0] < self.width and pos[1] < self.height:
            gap = self.width / 9
            x = pos[0] // gap
            y = pos[1] // gap
            return int(y), int(x)
        else:
            return None

    def is_finished(self):
        """
        Checks if the board is completed.
        """
        for i in range(self.rows):
            for j in range(self.cols):
                if self.cubes[i][j].value == 0:
                    return False
        return True


def redraw_window(win, board, time, strikes):
    win.fill((255, 255, 255))

    # Draw time
    font = pygame.font.SysFont("comicsans", 20)
    text = font.render(f"TIME:{format_time(time)}", True, (0, 0, 0))
    win.blit(text, (540-160, 560))

    # Draw Strikes
    text = font.render("X " * strikes, True, (255, 0, 0))
    win.blit(text, (20, 560))

    # Draw grid and board
    board.draw(win)


def format_time(secs):
    sec = secs % 60
    minute = secs//60
    hour = minute//60

    time = f" {str(minute)}: {str(sec)}"
    return time

def main():

    win = pygame.display.set_mode((540, 600))
    pygame.display.set_caption("SUDOKU")

    board = Grid(9, 9, 540, 540)
    key = None
    run = True
    start = time.time()
    strikes = 0
    while run:

        play_time = round(time.time() - start)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    key = 1
                if event.key == pygame.K_2:
                    key = 2
                if event.key == pygame.K_3:
                    key = 3
                if event.key == pygame.K_4:
                    key = 4
                if event.key == pygame.K_5:
                    key = 5
                if event.key == pygame.K_6:
                    key = 6
                if event.key == pygame.K_7:
                    key = 7
                if event.key == pygame.K_8:
                    key = 8
                if event.key == pygame.K_9:
                    key = 9

                if event.key == pygame.K_DELETE:
                    board.clear()
                    key = None

                if event.key == pygame.K_RETURN:
                    i, j = board.selected
                    if board.cubes[i][j].temp != 0:
                        if board.place(board.cubes[i][j].temp):
                            print("Success!")
                            # if board.is_finished():
                            #     print("GAME OVER")
                            #     run = False
                        else:
                            print("Wrong!")
                            strikes += 1
                        key = None

                    if board.is_finished():
                        print("GAME OVER")
                        run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clicked = board.click(pos)
                if clicked:
                    board.select(clicked[0], clicked[1])
                    key = None

        if board.selected and key is not None:
            board.sketch(key)

        redraw_window(win, board, play_time, strikes)
        pygame.display.update()


generate_board(default_board)
main()

pygame.quit()





