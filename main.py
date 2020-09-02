from graphics import *

PLAYS = 10


def main():
    win = GraphWin('MonteCarlo', 900, 900)  # pixels
    win.setCoords(0.0, 0.0, 100.0, 100.0)  # break into coordinates
    win.setBackground("white")

    point_start = Point(0, 0)
    point_end = Point(1, 1)

    draw_grid(win, 100)
    draw_square(win, point_start, point_end)

    plays = 0
    squares = {}
    while plays < PLAYS:
        p1 = win.getMouse()
        p1.draw(win)
        x = int(p1.getX())
        y = int(p1.getY())
        if (x, y) not in squares:
            square = draw_square(win, Point(x, y), Point(x+1, y+1))
            squares[(x, y)] = square
            print(p1)
            plays += 1


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


main()
