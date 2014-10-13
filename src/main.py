'''
Created on Oct 12, 2014

@author: Richard
'''
import pygame, sys, customization
from pygame.locals import QUIT
from functions import set_up_pygame, initialize_screen

set_up_pygame()
screen = initialize_screen()
background = customization.INIT_BACKGROUND

while True:
    screen.fill(background)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
