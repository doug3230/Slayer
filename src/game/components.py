'''
Created on Oct 18, 2014

@author: Richard
'''
import pygame

class Values:
    SCREEN_GRID = None
    CLOCK = None
    BACKGROUND = None
    STATE = None

def set_up_pygame():
    from customization import INIT_CENTERED, INIT_SCREEN_POSITION
    from os import environ
    if INIT_CENTERED:
        environ['SDL_VIDEO_CENTERED'] = '1'
    else:
        environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % INIT_SCREEN_POSITION
    pygame.init()
    return

def initialize_screen():
    from customization import DISPLAY_DOUBLE_BUFFERED, DISPLAY_RESIZABLE, \
    DISPLAY_CAPTION, INIT_SCREEN_SIZE, INIT_BACKGROUND
    from pygame.locals import DOUBLEBUF, RESIZABLE
    flags = 0
    if DISPLAY_DOUBLE_BUFFERED:
        flags |= DOUBLEBUF
    if DISPLAY_RESIZABLE:
        flags |= RESIZABLE
    pygame.display.set_caption(DISPLAY_CAPTION)
    #pygame.display.set_icon(load_image(customization.DISPLAY_ICON))
    screen = pygame.display.set_mode(INIT_SCREEN_SIZE, flags)
    screen.fill(INIT_BACKGROUND)
    return screen

def initialize_screen_grid():
    from customization import DISPLAY_GRID_ROWS, DISPLAY_GRID_COLS
    from display import ScreenGrid
    Values.SCREEN_GRID = ScreenGrid(DISPLAY_GRID_ROWS, DISPLAY_GRID_COLS)
    return

def initialize_clock():
    Values.CLOCK = pygame.time.Clock()
    return

def initialize_background():
    from customization import INIT_BACKGROUND
    Values.BACKGROUND = INIT_BACKGROUND
    return

def initialize_state():
    from game_state import TitleState, BattleState
    Values.STATE = TitleState()
    return

def initialize():
    set_up_pygame()
    initialize_screen()
    initialize_screen_grid()
    initialize_clock()
    initialize_background()
    initialize_state()
    return
    
def screen():
    return pygame.display.get_surface()

def screen_grid():
    return Values.SCREEN_GRID

def clock():
    return Values.CLOCK

def background():
    return Values.BACKGROUND

def state():
    return Values.STATE

def refresh_screen():
    pygame.display.flip()
    return

def tick(time = None):
    if time == None:
        from customization import DISPLAY_CLOCK_TICKS
        time = DISPLAY_CLOCK_TICKS
    Values.CLOCK.tick(time)
    return

def set_state(new_state):
    Values.STATE = new_state
    return
