from astar import AStar
import sys
import math


def drawmaze(maze, set1=[], set2=[], c='#', c2='*'):
    """returns an ascii maze, drawing eventually one (or 2) sets of positions.
        useful to draw the solution found by the astar algorithm
    """
    set1 = list(set1)
    set2 = list(set2)
    lines = maze.strip().split('\n')
    width = len(lines[0])
    height = len(lines)
    result = ''
    for j in range(height):
        for i in range(width):
            if (i, j) in set1:
                result = result + c
            elif (i, j) in set2:
                result = result + c2
            else:
                result = result + lines[j][i]
        result = result + '\n'
    return result


class MazeSolver(AStar):

    """sample use of the astar algorithm. In this exemple we work on a maze made of ascii characters,
    and a 'node' is just a (x,y) tuple that represents a reachable position"""

    def __init__(self, maze):
        self.lines = maze.strip().split('\n')
        self.width = len(self.lines[0])
        self.height = len(self.lines)

    def heuristic_cost_estimate(self, n1, n2):
        """computes the 'direct' distance between two (x,y) tuples"""
        (x1, y1) = n1
        (x2, y2) = n2
        return math.hypot(x2 - x1, y2 - y1)

    def distance_between(self, n1, n2):
        """this method always returns 1, as two 'neighbors' are always adajcent"""
        return 1

    def neighbors(self, node):
        """ for a given coordinate in the maze, returns up to 4 adjacent(north,east,south,west)
            nodes that can be reached (=any adjacent coordinate that is not a wall)
        """
        x, y = node
        return[(nx, ny) for nx, ny in[(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]if 0 <= nx < self.width and 0 <= ny < self.height and self.lines[ny][nx] == ' ']



# generate an ascii maze
m = open('data/maze.txt', 'rt').read()

# what is the size of it?
w = len(m.split('\n')[0])
h = len(m.split('\n'))


def find_start_and_goal(m):
    """
    Finds start/goal position given a maze object
    :param m: maze object
    :return:
    """
    start = None
    goal = None
    for y, line in enumerate(m.split('\n')):
        if 'P' in line:
            goal = (line.index('P') + 1, y)
        if 'X' in line:
            start = (line.index('X') + 1, y)
    return start, goal


start, goal = find_start_and_goal(m)

# let's solve it
#start = (1, 1)  # we choose to start at the upper left corner
goal = (23, 21)
foundPath = MazeSolver(m).astar(start, goal)

# print the solution
print(drawmaze(m, list(foundPath)))
