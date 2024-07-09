"""imported modules"""
from node import Node
from maze import Maze
from a_star_search import a_star_search

# Grid from sample.txt
grid = [
    '############',
    '#S...#######',
    '#.....######',
    '#.......####',
    '##......####',
    '#####..G####',
    '######.#####',
    '############'
]

def main():
    """main function"""
    # Find the start and goal coordinates from the grid
    start_x, start_y = None, None
    goal_x, goal_y = None, None
    for i,_ in enumerate(grid):
        for j,_ in enumerate(grid[0]):
            if grid[i][j] == 'S':
                start_x, start_y = i, j
            elif grid[i][j] == 'G':
                goal_x, goal_y = i, j

    if start_x is None or start_y is None:
        print("Start not found in the grid.")
        return
    if goal_x is None or goal_y is None:
        print("Goal not found in the grid.")
        return

    start = Node(start_x, start_y, 'vertical')
    goal = Node(goal_x, goal_y, 'vertical')

    maze = Maze(grid)
    path = a_star_search(maze, start, goal)

    if path:
        print("Path found:", path)
    else:
        print("No path found")

if __name__ == "__main__":
    main()
