#
# Conway's Game of Life implementation for micro:bit
#

import random


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

    def execute(self):
        self.current_iteration += 1


# MicroPython dose not have __main__
goe = GameOfLife()
