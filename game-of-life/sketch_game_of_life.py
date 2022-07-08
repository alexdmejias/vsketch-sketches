import vsketch
import numpy as np
from typing import List


class Grid_Game_Of_Life():
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns

        self.next_state: List[int] = np.random.randint(2, size=rows * columns)
        self.state = self.next_state.copy()

    def __str__(self):
        output = ""

        index = 0
        for _ in range(self.rows):
            for __ in range(self.columns):
                output += "█" if self.state[index] else " "
                index += 1
            output += "\n"

        return output

    def calculate_alive_neighbors(self, cell_index, state):
        state_len = len(state)

        N = (cell_index - self.columns) % state_len
        E = (cell_index + 1) % state_len
        S = (cell_index + self.columns) % state_len
        W = (cell_index - 1) % state_len

        NE = (cell_index - self.columns + 1) % state_len
        SE = (cell_index + self.columns + 1) % state_len
        SW = (cell_index + self.columns - 1) % state_len
        NW = (cell_index - self.columns - 1) % state_len

        return state[N] + state[E] + state[S] + state[W] + state[NE] + state[SE] + state[SW] + state[NW]

    def apply_rules(self, is_alive: int, alive_neigbors):
        if (is_alive and (alive_neigbors == 2 or alive_neigbors == 3)):
            return 1
        elif (not is_alive and alive_neigbors == 3):
            return 1
        else:
            return 0

    def advance(self, evolutions=1):
        for _ in range(evolutions):
            self.state = self.next_state.copy()

            for index, is_alive in enumerate(self.state):
                alive_neigbors = self.calculate_alive_neighbors(
                    index, self.state)

                self.next_state[index] = self.apply_rules(
                    is_alive, alive_neigbors)


class GameOfLifeSketch(vsketch.SketchClass):
    # Sketch parameters:
    cell_size = vsketch.Param(0.5)
    evolution = vsketch.Param(1)
    rows = vsketch.Param(40)
    columns = vsketch.Param(40)

    def draw_x(self, vsk, x, y, size):
        vsk.line(x, y, x + size, y + size)
        vsk.line(x + size, y, x, y + size)

    def draw(self, vsk: vsketch.Vsketch) -> None:
        vsk.size("a4", landscape=False)
        vsk.scale("cm")
        game = Grid_Game_Of_Life(self.rows, self.columns)

        game.advance(self.evolution)

        for row in range(game.rows):
            for column in range(game.columns):

                index = (row * self.columns) + column

                if (game.state[index]):
                    vsk.square(row * self.cell_size, column *
                               self.cell_size, self.cell_size)
                    self.draw_x(vsk, row * self.cell_size, column *
                                self.cell_size, self.cell_size)

    def finalize(self, vsk: vsketch.Vsketch) -> None:
        vsk.vpype("linemerge linesimplify reloop linesort")


if __name__ == "__main__":
    GameOfLifeSketch.display()
