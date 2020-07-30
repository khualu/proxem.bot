import sys
import math
from datetime import datetime

import pygame as pg
from astar import AStar

from settings import *

# Stap 28 komt AI uit bij kind


class AiPlayer(pg.sprite.Sprite):
    def __init__(self, game, map_data):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(MINDARO)
        self.rect = self.image.get_rect()
        self.map_data = map_data
        self.x = None
        self.y = None

        # ai path
        self.step_last = None
        self.step = 0
        self.speed_default = 0.1
        self.speed = self.speed_default
        self.path = self.astar_solve()
        self.speed_child = 0.3
        self.speed_people = 0.2

    def walk_step(self):
        if self.step == 0:
            self.speed = self.speed_default

        elif self.step == 18:
            self.speed = self.speed_child

        elif self.step == 22:
            self.speed = self.speed_default

        elif self.step == 28:
            self.speed = self.speed_people

        elif self.step == 34:
            self.speed = self.speed_default

        elif self.step == 47:
            self.speed = self.speed_child

        elif self.step == 59:
            self.speed = self.speed_default

        elif self.step == 64:
            self.speed = self.speed_people

        if self.step >= len(self.path) - 1:
            self.step = 0

        if not self.step_last:
            self.x, self.y = self.path[self.step]
            self.step += 1
        else:
            if (datetime.now() - self.step_last).total_seconds() < self.speed:
                return

            self.step += 1
            self.x, self.y = self.path[self.step]

        self.step_last = datetime.now()

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

        self.walk_step()

    def astar_solve(self):
        # returns path solved by astar
        start, goal = self.find_start_and_goal()
        self.x = start[0]
        self.y = start[1]

        # clean map data, remove positions
        data = []
        for line in self.map_data:
            _line = ''
            for c in line:
                if c not in ['\n', ' ', '1', 'C', 'c', 'N', 'P']:
                    _line += ' '
                else:
                    _line += c
            data.append(_line)

        return list(MazeSolver(data).astar(start, goal))

    def find_start_and_goal(self):
        """
        Finds start/goal position given a maze object
        :param m: maze object
        :return:
        """
        start = None
        goal = None
        for y, line in enumerate(self.map_data):
            if 'X' in line:
                goal = (line.index('X'), y)
            if 'A' in line:
                start = (line.index('A'), y)
        return start, goal


class MazeSolver(AStar):
    # https://github.com/jrialland/python-astar/blob/master/src/test/maze/maze.py
    def __init__(self, maze):
        self.lines = maze
        self.width = len(self.lines[0])
        self.height = len(self.lines)

    def heuristic_cost_estimate(self, n1, n2):
        (x1, y1) = n1
        (x2, y2) = n2
        return math.hypot(x2 - x1, y2 - y1)

    def distance_between(self, n1, n2):
        return 1

    def neighbors(self, node):
        x, y = node
        return[(nx, ny) for nx, ny in[(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]if 0 <= nx < self.width and 0 <= ny < self.height and self.lines[ny][nx] == ' ']
