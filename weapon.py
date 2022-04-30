from data import *


class Enemy(pygame.sprite.Sprite):
    def __init__(self, position_fired, speed, bullet_image, damage, effect):
        super().__init__()
        self.image = pygame.image.load(bullet_image).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.pos = vec(position_fired)
        self.vel = vec(speed)
        self.damage = damage
        self.effect = effect
