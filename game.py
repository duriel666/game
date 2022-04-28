from player import*
from world import *


def start(run):
    world = World('testi.png')
    player = Player((ww/2, wh))
    while run:
        player.update()
