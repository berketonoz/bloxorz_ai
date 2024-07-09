class Node:
    def __init__(self, x, y, orientation, parent=None):
        self.x = x
        self.y = y
        self.orientation = orientation  # 'vertical', 'horizontal_h', or 'horizontal_v'
        self.parent = parent
        self.g = 0  # Cost from start to node
        self.h = 0  # Heuristic cost to goal
        self.f = 0  # Total cost

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.orientation == other.orientation

    def __lt__(self, other):
        return self.f < other.f

    def __hash__(self):
        return hash((self.x, self.y, self.orientation))