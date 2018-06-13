#
# Conway's Game of Life implementation for micro:bit
# https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
#

import random
from microbit import *


class GameOfLife:
    CELL_NUM = 7
    MAX_ITERATION = 100

    # MicroPython dose not have enum module
    cell_state = {
        'ALIVE': 0,
        'DEAD': 1,
        'DYING': 2
    }

    def __init__(self):
        self.current_iteration = 0

        # current_state is 2 dimensional array of CellState
        self.current_state = \
            [[GameOfLife.cell_state['DEAD'] for _ in range(GameOfLife.CELL_NUM)] for _ in range(GameOfLife.CELL_NUM)]

        for i in range(1, GameOfLife.CELL_NUM - 1):
            for j in range(1, GameOfLife.CELL_NUM - 1):
                self.current_state[i][j] = random.randint(0, 2)

        print("end of init")

    def count_alive_cell(self, x, y):
        alive_cell_num = 0

        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if (i, j) != (x, y) and self.current_state[i][j] == GameOfLife.cell_state['ALIVE']:
                    alive_cell_num += 1

        return alive_cell_num

    def update_cells(self):
        for i in range(1, GameOfLife.CELL_NUM - 1):
            for j in range(1, GameOfLife.CELL_NUM - 1):

                current_cell_state = self.current_state[i][j]
                alive_cell_num = self.count_alive_cell(i, j)

                if (current_cell_state == GameOfLife.cell_state['DEAD'] or
                    current_cell_state == GameOfLife.cell_state['DYING']) and alive_cell_num == 3:
                    self.current_state[i][j] = GameOfLife.cell_state['ALIVE']
                elif current_cell_state == GameOfLife.cell_state['ALIVE'] and alive_cell_num <= 1:
                    self.current_state[i][j] = GameOfLife.cell_state['DYING']
                elif current_cell_state == GameOfLife.cell_state['ALIVE'] and alive_cell_num >= 4:
                    self.current_state[i][j] = GameOfLife.cell_state['DYING']
                elif self.current_state[i][j] == GameOfLife.cell_state['DYING']:
                    self.current_state[i][j] = GameOfLife.cell_state['DEAD']

    def show_led(self):
        for i in range(1, GameOfLife.CELL_NUM - 1):
            for j in range(1, GameOfLife.CELL_NUM - 1):
                current_cell_state = self.current_state[i][j]

                if current_cell_state == GameOfLife.cell_state['ALIVE']:
                    display.set_pixel(i - 1, j - 1, 9)
                elif current_cell_state == GameOfLife.cell_state['DYING']:
                    display.set_pixel(i - 1, j - 1, 5)
                else:
                    display.set_pixel(i - 1, j - 1, 0)


# MicroPython dose not have __main__
goe = GameOfLife()

