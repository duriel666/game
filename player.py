from data import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        '''self.index2 = 1
        self.images2 = []
        for i in range(0, 3):
            self.images2.append(pygame.image.load(
                f'gfx/flame{str(i+1)}.png'))
        self.image2 = self.images2[self.index2].convert_alpha()
        self.mask2 = pygame.mask.from_surface(self.image2)
        self.rect2 = self.image2.get_rect()'''
        self.index = 5
        self.images = []
        for i in range(0, 9):
            self.images.append(pygame.image.load(
                f'gfx/plane{str(i+1)}.png'))
        self.image = self.images[self.index].convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.pos = vec(pos)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.score = 0
        self.friction = -0.06
        self.health = 1000
        self.acceleration_x = 0.8
        self.acceleration_y = 0.5
        self.weapons = []

    def move_x(self):
        key = pygame.key.get_pressed()

        if self.pos.x > 40 and self.pos.x < ww-40:
            if key[K_a]:
                self.acc.x = -self.acceleration_x
                if self.index > 0:
                    self.index -= 1
                '''if self.index <= 0:
                    self.index = len(self.images)-1'''
            elif key[K_d]:
                self.acc.x = self.acceleration_x
                if self.index < 8:
                    self.index += 1
                '''if self.index >= len(self.images):
                    self.index = 0'''
            else:
                self.acc.x = 0
                if self.index > 4:
                    self.index -= 1
                if self.index < 4:
                    self.index += 1

        self.image = self.images[self.index]

        self.acc.x += self.vel.x * self.friction
        self.vel.x += self.acc.x
        self.pos.x += self.vel.x + self.friction * self.acc.x

        self.rect.center = self.pos

    def move_y(self):
        key = pygame.key.get_pressed()
        if self.pos.y > 150 and self.pos.y < wh:
            if key[K_w]:
                self.acc.y = -self.acceleration_y
                #self.index2 = 0
            elif key[K_s]:
                self.acc.y = self.acceleration_y
                #self.index2 = 2
            else:
                self.acc.y = 0
                #self.index2 = 1

        self.acc.y += self.vel.y * self.friction
        self.vel.y += self.acc.y
        self.pos.y += self.vel.y + self.friction * self.acc.y

        self.rect.center = self.pos


class Flame(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.index = 1
        self.images = []
        for i in range(0, 3):
            self.images.append(pygame.image.load(
                f'gfx/flame{str(i+1)}.png'))
        self.image = self.images[self.index].convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.pos = vec(pos)

    def update(self, pos):
        self.rect.midbottom = pos+(0, 150)
        key = pygame.key.get_pressed()
        if key[K_w]:
            self.index = 0
        elif key[K_s]:
            self.index = 2
        else:
            self.index = 1

        self.image = self.images[self.index]
