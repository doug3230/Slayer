'''
Created on Oct 26, 2014

@author: Richard
'''
import pygame, game, customization

class System:
    SCREEN_GRID = None
    CLOCK = None
    BACKGROUND = None
    STATE = None

def screen():
    return pygame.display.get_surface()

def screen_grid():
    return System.SCREEN_GRID

def clock():
    return System.CLOCK

def background():
    return System.BACKGROUND

def state():
    return System.STATE

def resize_screen(new_size):
    customization.initialization_settings.INIT_SCREEN_SIZE = new_size
    game.initialization.initialize_screen()
    return

def refresh_screen():
    pygame.display.flip()
    return

def tick(fps = customization.display_settings.DISPLAY_FPS):
    System.CLOCK.tick(fps)
    return

def set_background(new_background):
    System.BACKGROUND = new_background
    return

def set_state(new_state):
    System.STATE = new_state
    return

