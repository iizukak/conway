#
# Conway's Game of Life implementation for micro:bit
# https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
#

import random
import microbit


class GameOfLife:
    CELL_NUM = 7

    # MicroPython dose not have enum module
    STATE = {
        'ALIVE': 0,
        'DEAD': 1,
        'DYING': 2
    }

    MODE = {
        'AUTO': 0,
        'MANUAL': 1
    }

    def __init__(self):
        self.current_iteration = 0
        self.current_mode = GameOfLife.MODE['AUTO']

        # current_state is 2 dimensional array of CellState
        self.current_states = \
            [[GameOfLife.STATE['DEAD'] for _ in range(GameOfLife.CELL_NUM)] for _ in range(GameOfLife.CELL_NUM)]
        for i in range(1, GameOfLife.CELL_NUM - 1):
            for j in range(1, GameOfLife.CELL_NUM - 1):
                self.current_states[i][j] = random.randint(0, 2)

        self.present_state = \
            [[GameOfLife.STATE['DEAD'] for _ in range(GameOfLife.CELL_NUM)] for _ in range(GameOfLife.CELL_NUM)]

    def count_alive_cell(self, x, y):
        alive_cell_num = 0

        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if (i, j) != (x, y) and self.current_states[i][j] == GameOfLife.STATE['ALIVE']:
                    alive_cell_num += 1

        return alive_cell_num

    def update_cells(self):
        self.save_present_state()
        for i in range(1, GameOfLife.CELL_NUM - 1):
            for j in range(1, GameOfLife.CELL_NUM - 1):

                current_cell_state = self.current_states[i][j]
                alive_cell_num = self.count_alive_cell(i, j)

                if (current_cell_state == GameOfLife.STATE['DEAD'] or
                    current_cell_state == GameOfLife.STATE['DYING']) and alive_cell_num == 3:
                    self.current_states[i][j] = GameOfLife.STATE['ALIVE']
                elif current_cell_state == GameOfLife.STATE['ALIVE'] and alive_cell_num <= 1:
                    self.current_states[i][j] = GameOfLife.STATE['DYING']
                elif current_cell_state == GameOfLife.STATE['ALIVE'] and alive_cell_num >= 4:
                    self.current_states[i][j] = GameOfLife.STATE['DYING']
                elif self.current_states[i][j] == GameOfLife.STATE['DYING']:
                    self.current_states[i][j] = GameOfLife.STATE['DEAD']

        self.show_led()

    def switch_mode(self):
        self.current_mode = GameOfLife.MODE['MANUAL']\
            if self.current_mode == GameOfLife.MODE['AUTO'] else GameOfLife.MODE['MANUAL']

    def show_led(self):
        for i in range(1, GameOfLife.CELL_NUM - 1):
            for j in range(1, GameOfLife.CELL_NUM - 1):
                current_cell_state = self.current_states[i][j]

                if current_cell_state == GameOfLife.STATE['ALIVE']:
                    microbit.display.set_pixel(i - 1, j - 1, 9)
                elif current_cell_state == GameOfLife.STATE['DYING']:
                    microbit.display.set_pixel(i - 1, j - 1, 5)
                else:
                    microbit.display.set_pixel(i - 1, j - 1, 0)

    def save_present_state(self):
        for i in range(GameOfLife.CELL_NUM):
            for j in range(GameOfLife.CELL_NUM):
                self.present_state[i][j] = self.current_states[i][j]

    def is_dead(self):
        for i in range(GameOfLife.CELL_NUM):
            for j in range(GameOfLife.CELL_NUM):
                if self.present_state[i][j] != self.current_states[i][j]:
                    return False
        return True


def main():
    goe = GameOfLife()

    while True:
        if microbit.button_a.is_pressed() and microbit.button_b.is_pressed() or\
                goe.current_mode == goe.MODE['AUTO'] and goe.is_dead():
            microbit.sleep(500)
            goe = GameOfLife()
        elif microbit.button_a.is_pressed():
            goe.update_cells()
        elif microbit.button_b.is_pressed():
            goe.switch_mode()
        elif goe.current_mode == goe.MODE['AUTO']:
            goe.update_cells()
        microbit.sleep(150)


main()
