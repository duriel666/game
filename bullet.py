from data import *
import math
import random


class Bullet(pygame.sprite.Sprite):
    def __init__(self, position_fired, target_pos, speed, bullet_image, damage, accuracy, effect):
        super().__init__()
        self.image = pygame.image.load(bullet_image).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.pos = vec(position_fired)
        self.target = vec(target_pos)
        self.damage = damage
        self.accuracy = accuracy
        accuracy_random = (random.randrange(
            self.accuracy, 1000+1000-self.accuracy))/1000
        self.effect = effect
        dis_x = self.target.x-self.pos.x
        dis_y = self.target.y-self.pos.y
        angle = math.atan2(-dis_y, dis_x)*accuracy_random
        self.speed_x = -speed*math.cos(angle)
        self.speed_y = -speed*math.sin(angle)
        image = self.image
        image2 = pygame.transform.scale(
            image, (self.width, self.height*speed/10))
        image3 = pygame.transform.rotate(image2, math.degrees(angle)+90)
        self.image = image3

    def update(self):
        self.pos = (self.pos[0]-self.speed_x, self.pos[1]+self.speed_y)
        self.rect.center = self.pos
