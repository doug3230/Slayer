'''
Created on Oct 18, 2014

@author: Richard
'''
import pygame, game, state, customization

def initialize_pygame():
    from os import environ
    if customization.initialization_settings.INIT_CENTERED:
        environ['SDL_VIDEO_CENTERED'] = '1'
    else:
        screen_position = customization.initialization_settings.INIT_SCREEN_POSITION
        environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % screen_position
    pygame.init()
    return

def initialize_caption():
    caption = customization.display_settings.DISPLAY_CAPTION
    if caption:
        pygame.display.set_caption(caption)
    return

def initialize_icon():
    icon = customization.display_settings.DISPLAY_ICON
    if icon:
        icon_image = game.file_processing.load_image(icon)
        pygame.display.set_icon(icon_image)
    return

def initialize_background():
    background = customization.initialization_settings.INIT_BACKGROUND
    if background:
        game.components.System.BACKGROUND = background
    return

def initialize_screen_grid():
    from grid import ScreenGrid
    rows = customization.display_settings.DISPLAY_GRID_ROWS
    cols = customization.display_settings.DISPLAY_GRID_COLS
    screen_grid = ScreenGrid(rows, cols)
    game.components.System.SCREEN_GRID = screen_grid
    return

def initialize_clock():
    clock = pygame.time.Clock()
    game.components.System.CLOCK = clock
    return

def initialize_state():
    game_state = state.State()
    game.components.System.STATE = game_state
    return

def initialize_screen():
    from pygame.locals import DOUBLEBUF, RESIZABLE
    flags = 0
    if customization.display_settings.DISPLAY_DOUBLE_BUFFERED:
        flags |= DOUBLEBUF
    if customization.display_settings.DISPLAY_RESIZABLE:
        flags |= RESIZABLE
    screen_size = customization.initialization_settings.INIT_SCREEN_SIZE
    pygame.display.set_mode(screen_size, flags)
    return

def initialize():
    initialize_pygame()
    initialize_caption()
    initialize_icon()
    initialize_screen_grid()
    initialize_clock()
    initialize_background()
    initialize_state()
    initialize_screen()
    return
