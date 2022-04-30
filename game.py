from player import *
from world import *
from data import *
from weapon import *


def startgame(run):
    #world = World('testi.png')
    player_one = Player((ww/2, wh-1))
    sprites = pygame.sprite.Group()
    sprites.add(player_one)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
            if event.type == pygame.QUIT:
                pygame.quit()
        screen.fill(black)
        sprites.update()
        sprites.draw(screen)
        player_one.move_x()
        player_one.move_y()
        pygame.display.flip()
        clock.tick(fps)
