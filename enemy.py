from data import *


class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, speed, enemy_image, damage, fire_rate):
        super().__init__()
        self.image = pygame.image.load(enemy_image).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.pos = vec(pos)
        self.vel = vec(speed)
        self.damage = damage
        self.fire_rate = fire_rate
