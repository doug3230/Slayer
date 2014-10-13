'''
Created on Oct 12, 2014

@author: Richard
'''
from functions import *
import sys
from pygame.locals import QUIT

set_up_pygame()
screen = initialize_screen()
clock = initialize_clock()
background = initialize_background()

while True:
    screen.fill(background)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    tick(clock)
