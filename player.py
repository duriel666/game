from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.index = 0
        self.images = []
        '''for i in range(0, 72):
            self.images.append(pygame.image.load(
                f'gfx/plane{str(i+1)}.png'))'''
        self.image = pygame.image.load('gfx/plane.png')
        #self.image = self.images[self.index].convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.pos = vec(pos[0], pos[1]+wh)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.jumping = False
        self.score = 0
        self.keys = 0
        self.friction = -0.08
        self.health = 1000
        self.acceleration = 0.4
        self.weapons = []

    def move(self):
        self.acc = vec(0, self.gravity)
        key = pygame.key.get_pressed()

        if key[K_a]:
            self.acc.x = -self.acceleration
            self.index -= 1
            if self.index <= 0:
                self.index = len(self.images)-1
        if key[K_d]:
            self.acc.x = self.acceleration
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0

        self.image = self.images[self.index]

        self.acc.x += self.vel.x * self.friction
        self.vel += self.acc
        self.pos += self.vel + self.gravity * self.acc

        self.rect.midbottom = self.pos

        sound_volume = -self.vel.y/40
        if sound_volume > 1:
            sound_volume = 1

    def jump(self):
        if not self.jumping:
            self.jumping = True
            self.vel.y = -17

    def cancel_jump(self):
        if self.jumping:
            if self.vel.y < -5:
                self.vel.y = -5
