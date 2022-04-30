from data import *


class Player(pygame.sprite.Sprite):
    def __init__(self, player_image, pos):
        super().__init__()
        self.index = 0
        self.images = []
        '''for i in range(0, 72):
            self.images.append(pygame.image.load(
                f'gfx/plane{str(i+1)}.png'))'''
        self.image = player_image.convert_alpha()
        #self.image = self.images[self.index].convert_alpha()
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
                '''self.index -= 1
                if self.index <= 0:
                    self.index = len(self.images)-1'''
            elif key[K_d]:
                self.acc.x = self.acceleration_x
                '''self.index += 1
                if self.index >= len(self.images):
                    self.index = 0'''
            else:
                self.acc.x = 0

        #self.image = self.images[self.index]

        self.acc.x += self.vel.x * self.friction
        self.vel.x += self.acc.x
        self.pos.x += self.vel.x + self.friction * self.acc.x

        self.rect.center = self.pos

    def move_y(self):
        key = pygame.key.get_pressed()
        if self.pos.y > 150 and self.pos.y < wh:
            if key[K_w]:
                self.acc.y = -self.acceleration_y
            elif key[K_s]:
                self.acc.y = self.acceleration_y
            else:
                self.acc.y = 0

        self.acc.y += self.vel.y * self.friction
        self.vel.y += self.acc.y
        self.pos.y += self.vel.y + self.friction * self.acc.y

        self.rect.midbottom = self.pos

    def jump(self):
        if not self.jumping:
            self.jumping = True
            self.vel.y = -17

    def cancel_jump(self):
        if self.jumping:
            if self.vel.y < -5:
                self.vel.y = -5
