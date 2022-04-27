from settings import *


class World(pygame.sprite.Sprite):
    def __init__(self, world_image):
        super().__init__()
        self.image = pygame.image.load(world_image).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.pos = vec(0, wh-self.height)
        self.vel = vec(0, 0)

    def scroll_x(self, speed):
        self.rect.topleft = self.pos
        self.pos.x += speed*((self.width-ww)/(gw-ww))

    def scroll_y(self, speed):
        self.rect.topleft = self.pos
        self.pos.y += speed*((self.height-wh)/(gh-wh))
