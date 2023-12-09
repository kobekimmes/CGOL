import pygame as pg
from Cell import Cell


class Board:

    def __init__(self, w, h, res):
        self.w = w
        self.h = h
        self.res = res
        self.old_board = [[Cell(self.res, i * self.res, j * self.res) for j in range(self.h // self.res)] for i in
                          range(self.w // self.res)]
        self.new_board = self.old_board
        self.row_dir = [-1, -1, -1, 0, 0, 1, 1, 1]
        self.col_dir = [-1, 0, 1, -1, 1, -1, 0, 1]
        self.checkpoint = []


    def update(self, x, y, old_board, new_board, alive):
        total = 0

        for z in range(8):
            if (-1 < x + self.row_dir[z] < len(old_board)) and (-1 < y + self.col_dir[z] < len(old_board[0])):
                total += old_board[x + self.row_dir[z]][y + self.col_dir[z]].alive

        if alive:
            if total > 3 or total < 2:
                new_board[x][y].kill()
        else:
            if total == 3:
                new_board[x][y].give_life()

        self.new_board = new_board

    def copy(self, new_board):
        self.old_board = new_board

    def eval(self):
        for i in range(len(self.old_board)):
            for j in range(len(self.old_board[i])):
                self.update(i, j, self.old_board, self.new_board, self.old_board[i][j].alive)

    def display(self, screen):
        screen.fill("black")

        for i in range(len(self.old_board)):
            for j in range(len(self.old_board[i])):
                self.old_board[i][j].show(screen)

    def print(self):
        for i in range(len(self.old_board)):
            print([self.old_board[j][i].alive for j in range(len(self.old_board[0]))])
        print("###")

    def mouse_hover(self, screen):
        x, y = pg.mouse.get_pos()[0], pg.mouse.get_pos()[1]
        i, j = x // self.res, y // self.res
        self.old_board[i][j].shade(screen)

    def mouse_click(self, stroke, h, w):
        x, y = pg.mouse.get_pos()[0], pg.mouse.get_pos()[1]
        i, j = x // self.res, y // self.res
        for k in range(8):
            for m in range(1, stroke+1):
                if i+((m//2)*(self.row_dir[k])) < w and i+((m//2)*(self.row_dir[k])) > -1 and j+((m//2)*(self.col_dir[k])) > -1 and j+((m//2)*(self.col_dir[k])) < h:
                    self.old_board[i+((m//2)*(self.row_dir[k]))][j+((m//2)*(self.col_dir[k]))].give_life()


    def kill_all(self):
        for i in range(len(self.old_board)):
            for j in range(len(self.old_board[0])):
                self.old_board[i][j].kill()


    def save(self):
        self.checkpoint = self.old_board


    def load(self):
        self.old_board = self.checkpoint if self.checkpoint else self.old_board

