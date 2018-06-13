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
    state = {
        'ALIVE': 0,
        'DEAD': 1,
        'DYING': 2
    }

    mode = {
        'AUTO': 0,
        'MANUAL': 1
    }

    def __init__(self):
        self.current_iteration = 0
        self.current_mode = GameOfLife.mode['AUTO']

        # current_state is 2 dimensional array of CellState
        self.current_state = \
            [[GameOfLife.state['DEAD'] for _ in range(GameOfLife.CELL_NUM)] for _ in range(GameOfLife.CELL_NUM)]
        for i in range(1, GameOfLife.CELL_NUM - 1):
            for j in range(1, GameOfLife.CELL_NUM - 1):
                self.current_state[i][j] = random.randint(0, 2)

        self.present_state = \
            [[GameOfLife.state['DEAD'] for _ in range(GameOfLife.CELL_NUM)] for _ in range(GameOfLife.CELL_NUM)]

        print("end of init")

    def count_alive_cell(self, x, y):
        alive_cell_num = 0

        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if (i, j) != (x, y) and self.current_state[i][j] == GameOfLife.state['ALIVE']:
                    alive_cell_num += 1

        return alive_cell_num

    def update_cells(self):
        self.save_present_state()
        for i in range(1, GameOfLife.CELL_NUM - 1):
            for j in range(1, GameOfLife.CELL_NUM - 1):

                current_cell_state = self.current_state[i][j]
                alive_cell_num = self.count_alive_cell(i, j)

                if (current_cell_state == GameOfLife.state['DEAD'] or
                    current_cell_state == GameOfLife.state['DYING']) and alive_cell_num == 3:
                    self.current_state[i][j] = GameOfLife.state['ALIVE']
                elif current_cell_state == GameOfLife.state['ALIVE'] and alive_cell_num <= 1:
                    self.current_state[i][j] = GameOfLife.state['DYING']
                elif current_cell_state == GameOfLife.state['ALIVE'] and alive_cell_num >= 4:
                    self.current_state[i][j] = GameOfLife.state['DYING']
                elif self.current_state[i][j] == GameOfLife.state['DYING']:
                    self.current_state[i][j] = GameOfLife.state['DEAD']

    def switch_mode(self):
        self.current_mode = GameOfLife.mode['MANUAL']\
            if self.current_mode == GameOfLife.mode['AUTO'] else GameOfLife.mode['MANUAL']

    def show_led(self):
        for i in range(1, GameOfLife.CELL_NUM - 1):
            for j in range(1, GameOfLife.CELL_NUM - 1):
                current_cell_state = self.current_state[i][j]

                if current_cell_state == GameOfLife.state['ALIVE']:
                    display.set_pixel(i - 1, j - 1, 9)
                elif current_cell_state == GameOfLife.state['DYING']:
                    display.set_pixel(i - 1, j - 1, 5)
                else:
                    display.set_pixel(i - 1, j - 1, 0)

    def save_present_state(self):
        for i in range(GameOfLife.CELL_NUM - 2):
            for j in range(GameOfLife.CELL_NUM - 2):
                self.present_state[i][j] = self.current_state[i][j]

    def is_dead(self):
        for i in range(GameOfLife.CELL_NUM - 2):
            for j in range(GameOfLife.CELL_NUM - 2):
                if self.present_state[i][j] != self.current_state[i][j]:
                    return False
        return True

    @staticmethod
    def show_flash():
        for i in range(GameOfLife.CELL_NUM - 2):
            for j in range(GameOfLife.CELL_NUM - 2):
                display.set_pixel(i, j, 9)


# MicroPython dose not have __main__
goe = GameOfLife()
goe.show_led()

while True:
    if button_a.is_pressed() and button_b.is_pressed() or goe.current_mode == goe.mode['AUTO'] and goe.is_dead():
        sleep(500)
        # goe.show_flash()
        goe = GameOfLife()
        goe.show_led()
    elif button_a.is_pressed():
        goe.update_cells()
        goe.show_led()
    elif button_b.is_pressed():
        goe.switch_mode()
    elif goe.current_mode == goe.mode['AUTO']:
        goe.update_cells()
        goe.show_led()
    sleep(150)
