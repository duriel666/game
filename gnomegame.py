import pygame as pg
from pygame.locals import *

pg.init()
pg.font.init()
pg.mixer.init()

vec = pg.Vector2
clock = pg.time.Clock()

gw = 600
gh = 1080

screen = pg.display.set_mode(((gw, gh)), pg.RESIZABLE)
pg.display.set_caption('Gnome Hole - v0.1')

fps = 60
black = (0,  0,  0, 200)
white = (255, 255, 255, 200)
gnome_image = pg.image.load("game\gnomedata\gnome.png")


class Gnome(pg.sprite.Sprite):
    def __init__(self, gnome_img):
        super().__init__()
        self.image = gnome_img.convert_alpha()
        self.mask = pg.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.pos = vec(0, gh-(gh/5))
        self.vel = vec(0, 0)
        self.move_right = True
        self.launch = False

    def move(self):
        self.rect.center = self.pos
        self.vel.x = 0
        if not self.launch:
            if self.move_right:
                self.vel.x = 10
                if self.pos.x > gw:
                    self.move_right = False
            if not self.move_right:
                self.vel.x = -10
                if self.pos.x < 0:
                    self.move_right = True
        if self.launch:
            self.vel.x = 0
            self.vel.y = -20

        self.pos = self.pos+self.vel


def start_game(run):
    player = Gnome(gnome_image)
    sprites = pg.sprite.Group()
    sprites.add(player)
    while run:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    run = False
                if event.key == pg.K_SPACE:
                    player.launch = True
            elif event.type == pg.QUIT:
                pg.quit()

        screen.fill(black)
        sprites.draw(screen)
        player.move()
        pg.display.flip()
        clock.tick(fps)


if __name__ == "__main__":
    start_game(True)
