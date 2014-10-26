'''
Created on Oct 25, 2014

@author: Richard
'''
import pygame
from elements import TileShape
from pygame.font import SysFont
from game import drawText

class Rectangle(TileShape):
    def __init__(self, colour = (0, 0, 0), thickness = 0, x_index = 0, y_index = 0, x_tiles = 1, y_tiles = 1):
        TileShape.__init__(self, x_index, y_index, x_tiles, y_tiles)
        self.colour = colour
        self.thickness = thickness
        return
    
    def draw_to_screen(self, screen):
        TileShape.draw_to_screen(self, screen)
        rect = pygame.Rect(self.location, (self.width(), self.height()))
        pygame.draw.rect(screen, self.colour, rect, self.thickness)
        return
    
class FullScreenRectangle(Rectangle):
    def __init__(self, colour = (0, 0, 0), thickness = 10):
        Rectangle.__init__(self, colour, thickness, x_index = 0, y_index = 0, x_tiles = 10, y_tiles = 10)
        return

class TextBox(TileShape):
    def __init__(self, text = "", font = SysFont(None, 50), colour = (0, 0, 0), x_index = 0, y_index = 0, x_tiles = 1, y_tiles = 1):
        TileShape.__init__(self, x_index, y_index, x_tiles, y_tiles)
        self.text = text
        self.colour = colour
        self.font = font
        return
    
    def draw_to_screen(self, screen):
        TileShape.draw_to_screen(self, screen)
        rect = pygame.Rect(self.location, (self.width(), self.height()))
        
        drawText(screen, self.text, self.colour, rect, self.font)
        return