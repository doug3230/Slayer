'''
Created on Oct 18, 2014

@author: Richard
'''
import os, pygame, display
from customization import *

class Location:
    cur_x_index = 0
    cur_y_index = 0
    
    @staticmethod
    def center_x_index():
        return Location.cur_x_index + screen_grid().cols // 2
    
    @staticmethod
    def center_y_index():
        return Location.cur_y_index + screen_grid().rows // 2
    
    @staticmethod
    def set_center_x_index(x_index):
        Location.cur_x_index = x_index - screen_grid().cols // 2
        
    @staticmethod
    def set_center_y_index(y_index):
        Location.cur_y_index = y_index - screen_grid().rows // 2

class Values:
    SCREEN_GRID = None
    CLOCK = None
    BACKGROUND = None

def initialize():
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
        pygame.display.set_caption(customization.DISPLAY_CAPTION)
        #pygame.display.set_icon(load_image(customization.DISPLAY_ICON))
        screen = pygame.display.set_mode(customization.INIT_SCREEN_SIZE, flags)
        screen.fill(customization.INIT_BACKGROUND)
        return screen

    def initialize_screen_grid():
        Values.SCREEN_GRID = display.ScreenGrid(customization.DISPLAY_GRID_ROWS, customization.DISPLAY_GRID_COLS)
        return
    
    def initialize_clock():
        Values.CLOCK = pygame.time.Clock()
        return
    
    def initialize_background():
        Values.BACKGROUND = customization.INIT_BACKGROUND
        return
    
    set_up_pygame()
    initialize_screen()
    initialize_screen_grid()
    initialize_clock()
    initialize_background()
    return
    
def screen():
    return pygame.display.get_surface()

def screen_grid():
    return Values.SCREEN_GRID

def clock():
    return Values.CLOCK

def background():
    return Values.BACKGROUND

def tick(time = customization.DISPLAY_CLOCK_TICKS):
    Values.CLOCK.tick(time)
    return

def load_music(file_name, path_included = False):
    if not path_included:
        pygame.mixer.music.load(path_to_music(file_name))
    else:
        pygame.mixer.music.load(file_name)
    return

def play_music(loop = True):
    if loop:
        pygame.mixer.music.play(-1)
    else:
        pygame.mixer.music.play()
    return
    
def stop_music():
    pygame.mixer.music.stop()
    return

def load_image(file_name, path_included = False):
    if not path_included:
        image = pygame.image.load(path_to_image(file_name))
    else:
        image = pygame.image.load(file_name)
    return image.convert()

def resize_image(image, new_width, new_height):
    image = pygame.transform.scale(image, (new_width, new_height))
    return image.convert()

def path_to_image(file_name):
    return "files/images/{0}".format(file_name)

def path_to_music(file_name):
    return "files/music/{0}".format(file_name)

def path_to_level(file_name):
    return "files/levels/{0}".format(file_name)
