#
# Conway's Game of Life implementation for micro:bit
#

from enum import Enum, auto
import random


class GameOfLife:
    CELL_NUM = 7
    MAX_ITERATION = 100

    class CellState(Enum):
        ALIVE = auto()
        DEAD = auto()
        DYING = auto()

    def __init__(self):
        self.current_iteration = 0

        # current_state is 2 dimensional array of CellState
        self.current_state = \
            [[GameOfLife.CellState.DEAD for _ in range(GameOfLife.CELL_NUM)] for _ in range(GameOfLife.CELL_NUM)]

        for i in range(1, GameOfLife.CELL_NUM - 1):
            for j in range(1, GameOfLife.CELL_NUM - 1):
                self.current_state[i][j] = random.choice(list(GameOfLife.CellState))

    def execute(self):
        self.current_iteration += 1


if __name__ == '__main__':
    g = GameOfLife().current_state
    print(g)
