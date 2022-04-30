from player import *
from world import *
from data import *
from weapon import *


def startgame(run):
    mouse = pygame.mouse.get_pos()
    #world = World('testi.png')
    player_one = Player((ww/2, wh-1))
    sprites = pygame.sprite.Group()
    sprites.add(player_one)
    weapon_one = Weapon((player_one.pos), (mouse),
                        100, 'gfx/bullet1.png', 10, 1)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                weapon_one()
        screen.fill(black)
        sprites.update()
        sprites.draw(screen)
        player_one.move_x()
        player_one.move_y()
        mouse = pygame.mouse.get_pos()
        pygame.display.flip()
        clock.tick(fps)
