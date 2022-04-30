from data import *


class World(pygame.sprite.Sprite):
    def __init__(self, world_image, pos):
        super().__init__()
        self.image = world_image.convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.pos = vec(pos)
        self.vel = vec(0, 0)

    def scroll_x(self, speed):
        self.rect.topleft = self.pos
        self.pos.x += speed*((self.width/2-ww)/(gw-ww))

    def scroll_y(self, speed):
        self.rect.topleft = self.pos
        self.pos.y += speed*((self.height/2-wh)/(gh-wh))

    def scrolling(self, speed):
        self.rect.topleft = self.pos
        self.pos += (0, speed)
