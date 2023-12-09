import pygame as pg
from Board import Board



class GameOfLife:

    def __init__(self, w, h, res, FPS):

        self.W, self.H = w, h
        self.res = res

        self.FPS = FPS

        self.board = Board(self.W, self.H, self.res)

        self.screen = pg.display.set_mode((self.W, self.H))

        self.clock = pg.time.Clock()
        self.running = True
        self.paused = False

    def loop(self, stroke=1):

        while self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_k:
                        self.board.kill_all()
                    if event.key == pg.K_p:
                        if not self.paused:
                            self.pause(True)
                        else:
                            self.pause(False)

                    if event.key == pg.K_s:
                        self.board.save()
                    if event.key == pg.K_l:
                        self.board.load()
                        self.board.display(self.screen)
                        self.board.print()


            if pg.mouse.get_pressed()[0]:

                self.board.mouse_click(stroke, self.H, self.W)

            self.board.display(self.screen)

            if not self.paused:
                self.board.eval()


            self.board.copy(self.board.new_board)
            self.board.mouse_hover(self.screen)

            pg.display.flip()

            self.clock.tick(self.FPS)

        pg.quit()


    def pause(self, pausing):
        self.paused = True if pausing else False


CGOL = GameOfLife(200, 200, 20, 60)
CGOL.loop(1)
