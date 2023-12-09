import random
import pygame as pg


class Cell:

    def __init__(self, size, x, y):
        self.x = x
        self.y = y
        self.size = size
        self.alive = random.randint(0,1)
        self.rect = pg.Rect(self.x, self.y, self.size, self.size)

    def show(self, screen):
        if self.alive:
            pg.draw.rect(screen, ("white"), self.rect)

    def kill(self):
        self.alive = 0

    def give_life(self):
        self.alive = 1

    def shade(self, screen):
        if self.alive:
            pg.draw.rect(screen, (255,0, 0, 0.75), self.rect)
        else:
            pg.draw.rect(screen, (255, 0, 0, 0.75), self.rect)




