'''
Created on Oct 13, 2014

@author: Richard
'''
import pygame.locals 
import os, customization

def set_up_pygame():
    if customization.INIT_CENTERED:
        os.environ['SDL_VIDEO_CENTERED'] = '1'
    else:
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % customization.INIT_SCREEN_POSITION
    pygame.init()
    return

def initialize_screen():
    flags = 0
    if customization.DISPLAY_DOUBLE_BUFFERED:
        flags |= pygame.locals.DOUBLEBUF
    if customization.DISPLAY_RESIZABLE:
        flags |= pygame.locals.RESIZABLE
    screen = pygame.display.set_mode(customization.INIT_SCREEN_SIZE, flags)
    screen.fill(customization.INIT_BACKGROUND)
    return screen
