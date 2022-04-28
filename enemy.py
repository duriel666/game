from data import *


class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemy_image, damage):
        super().__init__()
        self.image = pygame.image.load(enemy_image).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.pos = vec(0, wh-self.height)
        self.vel = vec(0, 0)
        self.damage = damage
