class Cell(object):

    def __init__(self, x: int, y: int, squares):
        self.x = x
        self.y = y
        self.squares = squares
        prev_x = self.x - 1
        prev_y = self.y - 1
        next_x = self.x + 1
        next_y = self.y + 1
        self.alive_neighbors = []
        self.dead_neighbors = []
        self.MAX_COORD = 100.0  # Coordinate size of window

        if prev_x >= 0 and prev_y >= 0:
            if (prev_x, prev_y) in squares:
                self.alive_neighbors.append((prev_x, prev_y))
            else:
                self.dead_neighbors.append((prev_x, prev_y))

        if next_x < self.MAX_COORD and next_y < self.MAX_COORD:
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

        if next_x < self.MAX_COORD:
            if (next_x, y) in squares:
                self.alive_neighbors.append((next_x, y))
            else:
                self.dead_neighbors.append((next_x, y))

        if prev_y < self.MAX_COORD:
            if (x, next_y) in squares:
                self.alive_neighbors.append((x, next_y))
            else:
                self.dead_neighbors.append((x, next_y))

        if next_x < self.MAX_COORD and prev_y >= 0:
            if (next_x, prev_y) in squares:
                self.alive_neighbors.append((next_x, prev_y))
            else:
                self.dead_neighbors.append((next_x, prev_y))

        if prev_x >= 0 and next_y < self.MAX_COORD:
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
