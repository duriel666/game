from player import *
from world import *
from data import *
from bullet import *

font = pygame.freetype.Font('stuff/NHaasGroteskTXPro-55Rg.ttf', 40)

pygame.mouse.set_visible(False)
cursor = pygame.image.load('gfx/cursor.png').convert_alpha()
cursor_rect = cursor.get_rect()


def startgame(run):
    mouse = pygame.mouse.get_pos()
    #world = World('testi.png')
    player_one = Player((ww/2, wh-1))
    sprites = pygame.sprite.Group()
    sprites.add(player_one)
    bullet_sprites = pygame.sprite.Group()
    bullet_list = []
    while run:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
            elif event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                bullet = Bullet((player_one.rect.center), (mouse),
                                50, 'gfx/bullet1.png', 2, 980, 1)
                bullet_list.append(bullet)
                bullet_sprites.add(bullet)
        screen.fill(black)
        sprites.update()
        sprites.draw(screen)
        bullet_sprites.draw(screen)
        for bullet in bullet_list:
            bullet.update()
            if not screen.get_rect().collidepoint(bullet.rect.center):
                bullet_list.remove(bullet)
        player_one.move_x()
        player_one.move_y()
        mouse = pygame.mouse.get_pos()
        font.render_to(
            screen, (10, 10), f'fps - {clock.get_fps():,.2f}', white)
        cursor_rect.center = pygame.mouse.get_pos()  # update position
        screen.blit(cursor, cursor_rect)
        pygame.display.flip()
        clock.tick(fps)
