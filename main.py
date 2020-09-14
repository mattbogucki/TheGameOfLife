from graphics import *
import random

from Cell import Cell

STARTING_CELL_COUNT = 1500  # Number of Cells to start simulation with
ITERATIONS = 10000           # Number of "years" to run


def main():
    win = GraphWin('Game Of Life', 900, 900)  # pixels 900x900
    win.setCoords(0.0, 0.0, 100.0, 100.0)  # break into coordinates 100x100
    win.setBackground("white")

    draw_grid(win, int(100.0))

    squares = {}

    for _ in range(STARTING_CELL_COUNT):
        x_rand = random.randrange(100)
        y_rand = random.randrange(100)
        if (x_rand, y_rand) not in squares:
            square = draw_square(win, Point(x_rand, y_rand), Point(x_rand+1, y_rand+1))
            squares[(x_rand, y_rand)] = square

    iterations = 0
    while iterations < ITERATIONS:
        iterations += 1
        dead_cells_that_have_been_checked = set()

        additions = []
        subtractions = []

        for coordinates, square in squares.items():
            x, y = coordinates

            this_cell = Cell(x, y, squares)
            # Any dead cell with three live neighbours becomes a live cell.
            for dead_neighbor in this_cell.get_dead_neighbors():
                if dead_neighbor not in dead_cells_that_have_been_checked:
                    dead_cells_that_have_been_checked.add(dead_neighbor)
                    x1, y1 = dead_neighbor
                    neighbor = Cell(x1, y1, squares)
                    if neighbor.get_alive_neighbor_count() == 3:
                        additions.append(dead_neighbor)

            # Any live cell with two or three live neighbours survives.
            # All other live cells die in the next generation. All other dead cells stay dead.
            alive_neighbors = this_cell.get_alive_neighbor_count()
            if alive_neighbors < 2 or alive_neighbors > 3:
                subtractions.append(coordinates)

        for cell in subtractions:
            square = squares[cell]
            square.undraw()
            squares.pop(cell, None)

        for cell2 in additions:
            new_x, new_y = cell2
            new_square = draw_square(win, Point(new_x, new_y), Point(new_x+1, new_y+1))
            squares[cell2] = new_square

    win.getMouse()
    win.close()


def draw_square(win: GraphWin, point_start: Point, point_end: Point) -> Rectangle:
    square = Rectangle(point_start, point_end)
    square.draw(win)
    square.setFill("black")
    return square


def draw_grid(win: GraphWin, n: int):
    for i in range(0, n):
        draw_line(win, Point(i, 0), Point(i, n))
        draw_line(win, Point(0, i), Point(n, i))


def draw_line(win: GraphWin, point_start: Point, point_end: Point):
    line = Line(point_start, point_end)
    line.draw(win)


if __name__ == "__main__":
    main()
