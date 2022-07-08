from random import randint
import vsketch
from dataclasses import dataclass
import numpy as np
import copy


class Cell:
    def __init__(self, row, column, index):
        self.row = row
        self.column = column
        self.index = index
        self.id = f"{row}-{column}"
        self.links = {}
        # self.valid_neighbors = 0
        self.neighbors = {
            "north": None,
            "northeast": None,
            "east": None,
            "southeast": None,
            "south": None,
            "southwest": None,
            "west": None,
            "northwest": None
        }

    def __str__(self):
        return f"r:{self.row}-c:{self.column}"

    def __repr__(self):
        return f"r:{self.row}-c:{self.column}"

    def link(self, cell, bilateral=True):
        self.links[cell.id] = cell

        if (bilateral):
            cell.link(self, False)

    def has_neighbor(self, direction):
        return self.neighbors.get(direction)

    def valid_neighbors(self):
        # return self.valid_neighbors
        return list(filter(None, self.neighbors.values()))
        # valid = []
        # for cell in self.neighbors:
        #     if (cell):
        #         valid.append(valid)

        # return valid

    def random_neighbor(self):
        return choice(list(filter(None, self.neighbors.values())))

    def is_linked(self, cell):
        if type(cell) == Cell:
            return cell.id in self.links
        return False


class Grid:
    def __init__(self, rows, columns, enhanced=False, cell_class=Cell):
        self.rows = rows
        self.columns = columns
        self.cell_class = cell_class
        self.grid: List[List[Cell]] = self.prepare_grid()
        self.configure_cells(enhanced)
        self.mutate()

    # def print(self):
    #     print(self.grid)

    def __str__(self):
        output = "+" + "---+" * self.columns + "\n"

        for row in self.each_row():
            top = "|"
            bottom = "+"

            for cell in row:
                # print(cell.links)
                body = f"   "

                east_boundry = " " if cell.is_linked(
                    cell.neighbors.get('east')) else "|"
                top += body + east_boundry
                south_boundry = "   " if cell.is_linked(
                    cell.neighbors.get('south')) else "---"
                bottom += south_boundry + "+"

            output += top + "\n"
            output += bottom + "\n"

        return output

    def size(self):
        return self.rows * self.columns

    def prepare_grid(self):
        grid = []
        cell_index = 0

        for row in range(self.rows):
            new_row = []
            for col in range(self.columns):
                cell_index += 1
                new_row.append(self.cell_class(row, col, cell_index))

            grid.append(new_row)
        return grid

    def __getitem__(self, pos):
        x, y = pos
        return "fetching %s, %s" % (x, y)

    def configure_cells(self, enhanced=False):
        for cell in self.each_cell():
            # valid_neighbors = 0

            if (cell.row > 0):
                cell.neighbors['north'] = self.grid[cell.row - 1][cell.column]
                # valid_neighbors += 1

            if (cell.row < self.rows - 1):
                cell.neighbors['south'] = self.grid[cell.row + 1][cell.column]
                # valid_neighbors += 1

            if (cell.column > 0):
                cell.neighbors['west'] = self.grid[cell.row][cell.column - 1]
                # valid_neighbors += 1

            if (cell.column < self.columns - 1):
                cell.neighbors['east'] = self.grid[cell.row][cell.column + 1]
                # valid_neighbors += 1

            if (enhanced):
                if (cell.has_neighbor('north') and cell.has_neighbor('east')):
                    cell.neighbors['northeast'] = self.grid[cell.row -
                                                            1][cell.column + 1]
                    # valid_neighbors += 1

                if (cell.has_neighbor('south') and cell.has_neighbor('east')):
                    cell.neighbors['southeast'] = self.grid[cell.row +
                                                            1][cell.column + 1]
                    # valid_neighbors += 1

                if (cell.has_neighbor('south') and cell.has_neighbor('west')):
                    cell.neighbors['southwest'] = self.grid[cell.row +
                                                            1][cell.column - 1]
                    # valid_neighbors += 1

                if (cell.has_neighbor('nort') and cell.has_neighbor('west')):
                    cell.neighbors['northwest'] = self.grid[cell.row -
                                                            1][cell.column - 1]
                    # valid_neighbors += 1

            # cell.valid_neighbors = valid_neighbors

    def each_row(self):
        for row in self.grid:
            yield row

    def each_cell(self):
        for row in self.each_row():
            for cell in row:
                yield cell

    def random_cell(self):
        row = choice(self.grid)
        cell = choice(row)

        return cell

    def mutate(self):
        pass


opposites = {
    "north"
    "northeast"
    "east"
    "southeast"
    "south"
    "southwest"
    "west"
    "northwest"
}


class Cell_Game_Of_Life(Cell):
    def __init__(self, row, column, cell_index):
        super().__init__(row, column, cell_index)
        self.is_alive = randint(0, 1)

    def __str__(self):
        return f"{self.is_alive}"

    def __repr__(self):
        return f"{self.is_alive}"

    def calculate_alive_neighbors(self):
        qty = 0
        for cell in self.valid_neighbors():
            if (cell.is_alive):
                qty += 1

        return qty


class Grid_Game_Of_Life(Grid):
    def __init__(self, rows, columns):
        super().__init__(rows, columns, True, Cell_Game_Of_Life)
        self.next_state = self.get_grid_state()
        self.state = copy.copy(self.next_state)

    def __str__(self):
        output = "+" + "---+" * self.columns + "\n"

        for row in self.each_row():
            top = "|"
            bottom = "+"

            for cell in row:
                body = f" {cell.is_alive} "

                east_boundry = " " if cell.is_linked(
                    cell.neighbors.get('east')) else "|"
                top += body + east_boundry
                south_boundry = "   " if cell.is_linked(
                    cell.neighbors.get('south')) else "---"
                bottom += south_boundry + "+"

            output += top + "\n"
            output += bottom + "\n"

        return output

    def prepare_grid(self):
        grid = []

        cell_index = 0

        for row in range(self.rows):
            new_row = []
            for col in range(self.columns):
                cell_index += 1
                new_row.append(self.cell_class(row, col, cell_index))

            grid.append(new_row)
        return grid

    def get_grid_state(self):
        state = []
        for cell in self.each_cell():
            state.append(cell.is_alive)

        return state

    def advance(self):
        index = 0
        for cell in self.each_cell():

            alive = cell.calculate_alive_neighbors()
            if (cell.is_alive and (alive == 2 or alive == 3)):
                self.next_state[index] = 1
                print("changed here", index)
            elif (not cell.is_alive and alive == 3):
                self.next_state[index] = 1
            else:
                self.next_state[index] = 0

            index += 1


class VectorsSketch(vsketch.SketchClass):
    # Sketch parameters:
    # radius = vsketch.Param(2.0)

    def draw(self, vsk: vsketch.Vsketch) -> None:
        vsk.size("a4", landscape=False)
        vsk.scale("cm")

        # g = Grid(4, 4, True)
        # max = 8
        # print(g)
        # direction = 'northeast'

        # cell = g.grid[1][0]
        # cells = [cell]

        # for i in range(8):
        #     new_cell = cell.has_neighbor(direction)
        #     if (new_cell):
        #         print('wasd')
        #         # draw line
        #         cell = new_cell

        grid = Grid_Game_Of_Life(10, 10)
        cell = grid.grid[0][1]

        # state = []
        # next_state = []
        # for cell in grid.each_cell():
        #     next_state.append(cell.is_alive)

        # state = copy.copy(next_state)

        print(grid)
        grid.advance()
        print(grid)

    def finalize(self, vsk: vsketch.Vsketch) -> None:
        vsk.vpype("linemerge linesimplify reloop linesort")


if __name__ == "__main__":
    VectorsSketch.display()
