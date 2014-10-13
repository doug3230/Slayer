'''
Created on Oct 12, 2014

@author: Richard
'''
import pygame, os, sys
from pygame.locals import HWSURFACE, DOUBLEBUF, RESIZABLE, QUIT

SCREEN_SIZE = (800, 600)
WHITE = (255, 255, 255)

os.environ['SDL_VIDEO_CENTERED'] = '1'  # center the window 
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE, HWSURFACE | DOUBLEBUF | RESIZABLE)
screen.fill(WHITE)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
