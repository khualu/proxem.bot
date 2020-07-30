import pygame as pg
from settings import TILESIZE, GINGER, PINKU

class Child (pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.child
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(PINKU)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Person (pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.person
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(GINGER)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
