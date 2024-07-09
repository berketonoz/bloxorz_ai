import heapq

class Node:
    def __init__(self, x, y, parent=None):
        self.x = x
        self.y = y
        self.parent = parent
        self.g = 0  # Cost from start to node
        self.h = 0  # Heuristic cost to goal
        self.f = 0  # Total cost

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return self.f < other.f

class Maze:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])

    def get_neighbors(self, node):
        neighbors = []
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            x, y = node.x + dx, node.y + dy
            if 0 <= x < self.rows and 0 <= y < self.cols and self.grid[x][y] != '#':
                neighbors.append(Node(x, y))
        return neighbors

def heuristic(node, goal):
    return abs(node.x - goal.x) + abs(node.y - goal.y)

def a_star_search(maze, start, goal):
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            return reconstruct_path(came_from, current)

        for neighbor in maze.get_neighbors(current):
            tentative_g_score = g_score[current] + 1

            if tentative_g_score < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                if neighbor not in open_set:
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return []

def reconstruct_path(came_from, current):
    path = []
    while current in came_from:
        path.append((current.x, current.y))
        current = came_from[current]
    path.reverse()
    return path

# Example usage:
grid = [
    ['S', '.', '.', '#', '.', '.', '.'],
    ['.', '#', '.', '.', '.', '#', '.'],
    ['.', '#', '.', '.', '.', '.', '.'],
    ['.', '.', '#', '#', '.', '.', '.'],
    ['#', '.', '#', 'G', '.', '#', '.']
]

start = Node(0, 0)  # Starting point 'S'
goal = Node(4, 3)   # Goal point 'G'

maze = Maze(grid)
path = a_star_search(maze, start, goal)

if path:
    print("Path found:", path)
else:
    print("No path found")
