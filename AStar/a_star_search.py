"""imported modules"""
import heapq

def heuristic(node, goal):
    """Heuristic calculation of total distance to goal"""
    return abs(node.x - goal.x) + abs(node.y - goal.y)

def a_star_search(maze, start, goal):
    """a star search algorithm implementation"""
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current.x == goal.x and current.y == goal.y and current.orientation == 'vertical':
            return reconstruct_path(came_from, current)

        for neighbor in maze.get_neighbors(current):
            tentative_g_score = g_score[current] + 1

            if tentative_g_score < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                if all(neighbor != n for _, n in open_set):
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return []

def reconstruct_path(came_from, current):
    """function for path recovery"""
    path = []
    while current in came_from:
        path.append((current.x, current.y, current.orientation))
        current = came_from[current]
    path.reverse()
    return path
