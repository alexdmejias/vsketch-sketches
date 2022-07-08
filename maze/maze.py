from random import choice
from typing import cast, Generator, List, Optional, Tuple


class Cell:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.id = f"{row}-{column}"
        self.links = {}
        self.neighbors = {
            "north": None,
            "east": None,
            "south": None,
            "west": None
        }

    def __str__(self):
        return f"r:{self.row}||c:{self.column}"

    def __repr__(self):
        return f"r:{self.row}||c:{self.column}"

    def link(self, cell, bilateral=True):
        self.links[cell.id] = cell

        if (bilateral):
            cell.link(self, False)

    def random_neighbor(self):
        return choice(list(filter(None, self.neighbors.values())))

    def is_linked(self, cell):
        if type(cell) == Cell:
            return cell.id in self.links
        return False


class Grid:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.grid: List[List[Cell]] = self.prepare_grid()
        self.configure_cells()
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

        for row in range(self.rows):
            new_row = []
            for col in range(self.columns):
                new_row.append(Cell(row, col))

            grid.append(new_row)
        return grid

    def __getitem__(self, pos):
        x, y = pos
        return "fetching %s, %s" % (x, y)

    def configure_cells(self):
        for cell in self.each_cell():

            if (cell.row > 0):
                cell.neighbors['north'] = self.grid[cell.row - 1][cell.column]

            if (cell.row < self.rows - 1):
                cell.neighbors['south'] = self.grid[cell.row + 1][cell.column]

            if (cell.column > 0):
                cell.neighbors['west'] = self.grid[cell.row][cell.column - 1]

            if (cell.column < self.columns - 1):
                cell.neighbors['east'] = self.grid[cell.row][cell.column + 1]

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

    def mutate():
        pass


class Binary(Grid):
    def mutate(self):
        for cell in self.each_cell():
            neighbors = []

            north_neighbor = cell.neighbors['north']
            east_neighbor = cell.neighbors['east']

            if (north_neighbor):
                neighbors.append(north_neighbor)

            if (east_neighbor):
                neighbors.append(east_neighbor)

            if (neighbors):
                random = choice(neighbors)
                cell.link(random)


class Sidewinder(Grid):
    def mutate(self):
        for row in self.each_row():
            run = []

            for cell in row:
                run.append(cell)
                at_eastern_boundary = cell.neighbors['east'] is None
                at_northern_boundary = cell.neighbors['north'] is None
                should_close_out = at_eastern_boundary or (
                    not at_northern_boundary and choice([True, False]))

                if should_close_out:
                    member = choice(run)

                    if member.neighbors['north']:
                        member.link(member.neighbors['north'])

                    run.clear()
                else:
                    if (cell.neighbors['east']):
                        cell.link(cell.neighbors['east'])


class AldousBroader(Grid):
    def mutate(self):
        cell = self.random_cell()
        unvisited = self.size() - 1

        while unvisited > 0:
            neighbor = cell.random_neighbor()

            if (not neighbor.links):
                cell.link(neighbor)
                unvisited -= 1

            cell = neighbor


# g = AldousBroader(20, 20)
# print(g)
