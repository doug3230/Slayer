'''
Created on Oct 31, 2014

@author: Richard
'''
import game, pygame
from elements import TileShape
from constants.colours import BLACK, WHITE
from customization.display_settings import DISPLAY_GRID_ROWS, DISPLAY_GRID_COLS

class Rectangle(TileShape):
    def __init__(self, colour=BLACK, background_colour=None, thickness=0, *args, **kwargs):
        TileShape.__init__(self, *args, **kwargs)
        self.colour = colour
        self.background_colour = background_colour
        self.thickness = thickness
        return
    
    def draw_to_screen(self, screen):
        TileShape.draw_to_screen(self, screen)
        rect = pygame.Rect(self.location, (self.width(), self.height()))
        if self.background_colour != None:
            pygame.draw.rect(screen, self.colour, rect)
            pygame.draw.rect(screen, self.background_colour, rect, self.thickness)
        else:
            pygame.draw.rect(screen, self.colour, rect, self.thickness)
        return

def full_screen_rectangle(colour=WHITE, background_colour=BLACK, thickness=0):
    return Rectangle(colour, background_colour, thickness, x_index=0, y_index=0, x_tiles=DISPLAY_GRID_COLS, y_tiles=DISPLAY_GRID_ROWS)

class TextBox(TileShape):
    def __init__(self, font, text, border_tiles=0, rectangle=None, font_colour=BLACK, **kwargs):
        if rectangle:
            kwargs['x_index'], kwargs['y_index'], kwargs['x_tiles'], kwargs['y_tiles'] = \
            rectangle.x_index, rectangle.y_index, rectangle.x_tiles, rectangle.y_tiles 
        TileShape.__init__(self, **kwargs)
        self.font = font
        self.text = text
        self.font_colour = font_colour
        self.border_tiles = border_tiles
        self.rectangle = rectangle
        return
    
    def draw_to_screen(self, screen):
        if self.rectangle:
            self.rectangle.draw_to_screen(screen)
        screen_grid = game.screen_grid()
        border_width = screen_grid.tile_width() * self.border_tiles
        border_height = screen_grid.tile_height() * self.border_tiles
        location = self.location
        location = (location[0] + border_width, location[1] + border_height)
        self.font.render_to(screen, location, self.text, self.font_colour)
        return

