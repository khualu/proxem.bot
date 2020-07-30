import pygame as pg
import sys
from settings import *
from spites.ai import AiPlayer
from spites.walls import Wall, Painting, Goal
from spites.player import Player
from spites.child import Child, Person
from os import path


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.map_data = []
        self.load_data()

        # user controlled player
        self.player = None

        # ai controlled player
        self.ai_player = None

    def load_data(self):
        map = open('data/map.txt', 'rt')
        self.map_data = [line.strip() for line in map.readlines()]
        map.close()

    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.child = pg.sprite.Group()
        self.childshadow = pg.sprite.Group()
        self.person = pg.sprite.Group()
        self.paintings = pg.sprite.Group()
        self.goals = pg.sprite.Group()

        self.ai_player = AiPlayer(self, self.map_data)

        for row, tiles in enumerate(self.map_data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row)
                if tile == 'C':
                    Child(self, col, row)
                if tile == 'N':
                    Person(self, col, row)
                if tile == 'P':
                    Painting(self, col, row)
                if tile == 'X':
                    Goal(self, col, row)
                # if tile == 'P':
                #     self.player = Player(self, col, row)


    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.key == pg.K_LEFT:
                    self.player.move(dx=-1)
                if event.key == pg.K_RIGHT:
                    self.player.move(dx=1)
                if event.key == pg.K_UP:
                    self.player.move(dy=-1)
                if event.key == pg.K_DOWN:
                    self.player.move(dy=1)

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass


# create the game object
g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
    g.show_go_screen()
