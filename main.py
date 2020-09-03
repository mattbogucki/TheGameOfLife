from graphics import *
import random

BLOCKS = 1500
ITERATIONS = 1000
MIN_COORD = 0.0
MAX_COORD = 100.0
TEST = 0


def main():
    win = GraphWin('Game Of Life', 900, 900)  # pixels
    win.setCoords(MIN_COORD, MIN_COORD, MAX_COORD, MAX_COORD)  # break into coordinates
    win.setBackground("white")

    draw_grid(win, int(MAX_COORD))

    plays = 0
    squares = {}
    # while plays < BLOCKS:
    #     p1 = win.getMouse()
    #     x_coord = int(p1.getX())
    #     y_coord = int(p1.getY())
    #     if (x_coord, y_coord) not in squares:
    #         square = draw_square(win, Point(x_coord, y_coord), Point(x_coord+1, y_coord+1))
    #         squares[(x_coord, y_coord)] = square
    #         print(p1)
    #         plays += 1

    block_count = random.randrange(1500)
    for _ in range(block_count):
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

        for coords, square in squares.items():
            x, y = coords

            nbr = Neighbor(x,y,squares)
            # Any dead cell with three live neighbours becomes a live cell.
            for dead_neighbor in nbr.get_dead_neighbors():
                if dead_neighbor not in dead_cells_that_have_been_checked:
                    dead_cells_that_have_been_checked.add(dead_neighbor)
                    x1, y1 = dead_neighbor
                    nbr2 = Neighbor(x1, y1, squares)
                    if nbr2.get_alive_neighbor_count() == 3:
                        additions.append(dead_neighbor)

            # Any live cell with two or three live neighbours survives.
            # All other live cells die in the next generation. Similarly, all other dead cells stay dead.
            alive_neighbors = nbr.get_alive_neighbor_count()
            if alive_neighbors < 2 or alive_neighbors > 3:
                subtractions.append(coords)

        for scell in subtractions:
            square = squares[scell]
            square.undraw()
            squares.pop(scell, None)

        for acell in additions:
            new_x, new_y = acell
            new_square = draw_square(win, Point(new_x, new_y), Point(new_x+1, new_y+1))
            squares[acell] = new_square


    win.getMouse()
    win.close()


class Neighbor(object):

    def __init__(self,x,y,squares):
        self.x = x
        self.y = y
        self.squares = squares
        prev_x = self.x - 1
        prev_y = self.y - 1
        next_x = self.x + 1
        next_y = self.y + 1
        self.alive_neighbors = []
        self.dead_neighbors = []

        if prev_x >= 0 and prev_y >= 0:
            if (prev_x, prev_y) in squares:
                self.alive_neighbors.append((prev_x, prev_y))
            else:
                self.dead_neighbors.append((prev_x, prev_y))

        if next_x < MAX_COORD and next_y < MAX_COORD:
            if (next_x, next_y) in squares:
                self.alive_neighbors.append((next_x, next_y))
            else:
                self.dead_neighbors.append((next_x, next_y))

        if prev_x >= 0:
            if (prev_x, y) in squares:
                self.alive_neighbors.append((prev_x, y))
            else:
                self.dead_neighbors.append((prev_x, y))

        if prev_y >= 0:
            if (x, prev_y) in squares:
                self.alive_neighbors.append((x, prev_y))
            else:
                self.dead_neighbors.append((x, prev_y))

        if next_x < MAX_COORD:
            if (next_x, y) in squares:
                self.alive_neighbors.append((next_x, y))
            else:
                self.dead_neighbors.append((next_x, y))

        if prev_y < MAX_COORD:
            if (x, next_y) in squares:
                self.alive_neighbors.append((x, next_y))
            else:
                self.dead_neighbors.append((x, next_y))

        if next_x < MAX_COORD and prev_y >= 0:
            if (next_x, prev_y) in squares:
                self.alive_neighbors.append((next_x, prev_y))
            else:
                self.dead_neighbors.append((next_x, prev_y))

        if prev_x >= 0 and next_y < MAX_COORD:
            if (prev_x, next_y) in squares:
                self.alive_neighbors.append((prev_x, next_y))
            else:
                self.dead_neighbors.append((prev_x, next_y))

        self.alive_neighbor_count = len(self.alive_neighbors)
        self.dead_neighbor_count = len(self.dead_neighbors)

    def get_dead_neighbors(self) -> [()]:
        return self.dead_neighbors.copy()

    def get_alive_neighbor_count(self) -> int:
        return self.alive_neighbor_count


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


main()
