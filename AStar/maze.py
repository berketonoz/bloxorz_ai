from node import Node


class Maze:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])

    def is_valid(self, x, y):
        return 0 <= x < self.rows and 0 <= y < self.cols and self.grid[x][y] != '#'


    def is_goal(self, x, y):
        return self.grid[x][y] == 'G'


    def get_neighbors(self, node):
        neighbors = []
        x, y, orientation = node.x, node.y, node.orientation

        if orientation == 'vertical':
            moves = [
                (1, 0, 'horizontal_h', 'right'), (-1, 0, 'horizontal_h', 'left'), 
                (0, 1, 'horizontal_v', 'up'), (0, -1, 'horizontal_v', 'down')
            ]
            for dx, dy, new_orientation, move in moves:
                nx, ny = x + dx, y + dy
                if new_orientation == 'horizontal_h' and self.is_valid(nx, y) and self.is_valid(nx + 1, y):
                    neighbors.append(Node(nx, y, new_orientation, move, node))
                elif new_orientation == 'horizontal_h' and self.is_valid(nx, y) and self.is_valid(nx - 1, y):
                    neighbors.append(Node(nx, y, new_orientation, move, node))
                elif new_orientation == 'horizontal_v' and self.is_valid(x, ny) and self.is_valid(x, ny + 1):
                    neighbors.append(Node(x, ny, new_orientation, move, node))
                elif new_orientation == 'horizontal_v' and self.is_valid(x, ny) and self.is_valid(x, ny - 1):
                    neighbors.append(Node(x, ny, new_orientation, move, node))
        elif orientation == 'horizontal_h':
            moves = [
                (2, 0, 'vertical', 'right'), (-2, 0, 'vertical', 'left'), 
                (0, 1, 'horizontal_h', 'up'), (0, -1, 'horizontal_h', 'down')
            ]
            for dx, dy, new_orientation, move in moves:
                nx, ny = x + dx, y + dy
                if new_orientation == 'vertical' and self.is_valid(nx, y):
                    neighbors.append(Node(nx, y, new_orientation, move, node))
                elif new_orientation == 'vertical' and self.is_valid(nx, y):
                    neighbors.append(Node(nx, y, new_orientation, move, node))
                elif new_orientation == 'horizontal_h' and self.is_valid(x, ny) and self.is_valid(x + 1, ny):
                    neighbors.append(Node(x, ny, new_orientation, move, node))
                elif new_orientation == 'horizontal_h' and self.is_valid(x, ny) and self.is_valid(x - 1, ny):
                    neighbors.append(Node(x, ny, new_orientation, move, node))
        elif orientation == 'horizontal_v':
            moves = [
                (0, 2, 'vertical', 'up'), (0, -2, 'vertical', 'down'), 
                (1, 0, 'horizontal_v', 'right'), (-1, 0, 'horizontal_v', 'left')
            ]
            for dx, dy, new_orientation, move in moves:
                nx, ny = x + dx, y + dy
                if new_orientation == 'vertical' and self.is_valid(x, ny):
                    neighbors.append(Node(x, ny, new_orientation, move, node))
                elif new_orientation == 'vertical' and self.is_valid(x, ny):
                    neighbors.append(Node(x, ny, new_orientation, move, node))
                elif new_orientation == 'horizontal_v' and self.is_valid(nx, y) and self.is_valid(nx + 1, y):
                    neighbors.append(Node(nx, y, new_orientation, move, node))
                elif new_orientation == 'horizontal_v' and self.is_valid(nx, y) and self.is_valid(nx - 1, y):
                    neighbors.append(Node(nx, y, new_orientation, move, node))

        return neighbors
    