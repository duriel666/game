from player import *
from world import *
from data import *
from bullet import *

font = pygame.freetype.Font('stuff/NHaasGroteskTXPro-55Rg.ttf', 40)

pygame.mouse.set_visible(False)
cursor = pygame.image.load('gfx/cursor.png').convert_alpha()
cursor_rect = cursor.get_rect()
world_test_image = pygame.image.load('gfx/bg-test.png')
#player_image = pygame.image.load('gfx/plane.png')
bullet_image = pygame.image.load('gfx/bullet1.png')


def startgame(run):
    #utofire, timer = pygame.USEREVENT+1, 100
    mouse = pygame.mouse.get_pos()
    #world = World('testi.png')
    #player_one = Player(player_image, (ww/2, wh-1))
    player_one = Player((ww/2, wh/2))
    flame = Flame((ww/2, wh/2))
    worlds = []
    worlds.append(World(world_test_image, (0, 0)))
    worlds.append(World(world_test_image, (0, -1080)))
    #worlds.append(World(world_test_image, (0, -2160)))
    sprites = pygame.sprite.Group()
    sprites.add(player_one)
    sprites_flame = pygame.sprite.Group()
    sprites_flame.add(flame)
    bullet_sprites = pygame.sprite.Group()
    world_sprites = pygame.sprite.Group()
    scrolling_speed = 1
    for world in worlds:
        world_sprites.add(world)
    bullet_list = []
    autofire = False
    shooting = 0
    fire_rate = 60
    while run:
        #pygame.time.set_timer(autofire, timer)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                if event.key == pygame.K_LCTRL:
                    scrolling_speed = 2
            elif event.type == KEYUP:
                if event.key == pygame.K_LCTRL:
                    scrolling_speed = 1
            elif event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                autofire = True
            elif event.type == pygame.MOUSEBUTTONUP:
                autofire = False
            elif event.type == pygame.MOUSEWHEEL:
                fire_rate += event.y*10

        screen.fill(black)
        world_sprites.draw(screen)
        for world in worlds:
            world.scrolling(scrolling_speed)
            if world.pos.y > 1080:
                worlds.remove(world)
                worlds.append(
                    World(world_test_image, (0, worlds[0].pos.y-1081)))
                world_sprites.add(worlds[1])
        sprites.update()
        sprites_flame.update(player_one.pos)
        sprites_flame.draw(screen)
        sprites.draw(screen)
        if autofire:
            if shooting > 60/(fire_rate/60):
                bullet = Bullet((player_one.rect.center), (mouse),
                                50, bullet_image, 2, 900, 1)
                bullet_list.append(bullet)
                bullet_sprites.add(bullet)
                shooting = 0
            shooting += 1
        bullet_sprites.draw(screen)
        for bullet in bullet_list:
            bullet.update()
            if not screen.get_rect().collidepoint(bullet.rect.center):
                bullet_list.remove(bullet)
        player_one.move_x()
        player_one.move_y()
        #flame.pos = player_one.pos
        mouse = pygame.mouse.get_pos()
        font.render_to(
            screen, (7, 13), f'fps - {clock.get_fps():,.2f}', black)
        font.render_to(
            screen, (7, 58), f'fire_rate - {fire_rate} per minute', black)
        font.render_to(
            screen, (7, 103), f'bullets - {len(bullet_sprites)}', black)
        font.render_to(
            screen, (10, 10), f'fps - {clock.get_fps():,.2f}', white)
        font.render_to(
            screen, (10, 55), f'fire_rate - {fire_rate} per minute', white)
        font.render_to(
            screen, (10, 100), f'bullets - {len(bullet_sprites)}', white)
        cursor_rect.center = pygame.mouse.get_pos()  # update position
        screen.blit(cursor, cursor_rect)
        pygame.display.flip()
        clock.tick(fps)
