import pygame
from pygame.locals import *
import time

pygame.init()
pygame.font.init()
pygame.mixer.init()

vec = pygame.Vector2
clock = pygame.time.Clock()

ww = 1600
wh = 900
gw = 1920
gh = 1080

screen = pygame.display.set_mode(((ww, wh)), pygame.RESIZABLE)
pygame.display.set_caption('Scrolling Shooter - v0.1')

fps = 60
black = (0,  0,  0, 200)
white = (255, 255, 255, 200)
