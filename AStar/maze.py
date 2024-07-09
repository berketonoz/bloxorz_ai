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
                (0, 1, 'horizontal_h'), (0, -1, 'horizontal_h'), 
                (1, 0, 'horizontal_v'), (-1, 0, 'horizontal_v')
            ]
            for dx, dy, new_orientation in moves:
                nx, ny = x + dx, y + dy
                if new_orientation == 'horizontal_h' and self.is_valid(x, y + 1) and self.is_valid(x, y + 2):
                    neighbors.append(Node(x, y + 1, new_orientation, node))
                elif new_orientation == 'horizontal_h' and self.is_valid(x, y - 1) and self.is_valid(x, y - 2):
                    neighbors.append(Node(x, y - 1, new_orientation, node))
                elif new_orientation == 'horizontal_v' and self.is_valid(x + 1, y) and self.is_valid(x + 2, y):
                    neighbors.append(Node(x + 1, y, new_orientation, node))
                elif new_orientation == 'horizontal_v' and self.is_valid(x - 1, y) and self.is_valid(x - 2, y):
                    neighbors.append(Node(x - 1, y, new_orientation, node))
        elif orientation == 'horizontal_h':
            moves = [
                (0, 2, 'vertical'), (0, -2, 'vertical'), 
                (1, 0, 'horizontal_h'), (-1, 0, 'horizontal_h')
            ]
            for dx, dy, new_orientation in moves:
                nx, ny = x + dx, y + dy
                if new_orientation == 'vertical' and self.is_valid(x, y + 2):
                    neighbors.append(Node(x, y + 2, new_orientation, node))
                elif new_orientation == 'vertical' and self.is_valid(x, y - 2):
                    neighbors.append(Node(x, y - 2, new_orientation, node))
                elif new_orientation == 'horizontal_h' and self.is_valid(x + 1, y) and self.is_valid(x + 1, y + 1):
                    neighbors.append(Node(x + 1, y, new_orientation, node))
                elif new_orientation == 'horizontal_h' and self.is_valid(x - 1, y) and self.is_valid(x - 1, y + 1):
                    neighbors.append(Node(x - 1, y, new_orientation, node))
        elif orientation == 'horizontal_v':
            moves = [
                (2, 0, 'vertical'), (-2, 0, 'vertical'), 
                (0, 1, 'horizontal_v'), (0, -1, 'horizontal_v')
            ]
            for dx, dy, new_orientation in moves:
                nx, ny = x + dx, y + dy
                if new_orientation == 'vertical' and self.is_valid(x + 2, y):
                    neighbors.append(Node(x + 2, y, new_orientation, node))
                elif new_orientation == 'vertical' and self.is_valid(x - 2, y):
                    neighbors.append(Node(x - 2, y, new_orientation, node))
                elif new_orientation == 'horizontal_v' and self.is_valid(x, y + 1) and self.is_valid(x + 1, y + 1):
                    neighbors.append(Node(x, y + 1, new_orientation, node))
                elif new_orientation == 'horizontal_v' and self.is_valid(x, y - 1) and self.is_valid(x + 1, y - 1):
                    neighbors.append(Node(x, y - 1, new_orientation, node))

        return neighbors
