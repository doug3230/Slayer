'''
Created on Oct 18, 2014

@author: Richard
'''
from game import screen

class ScreenGrid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        return
    
    def tile_width(self):
        screen_rect = screen().get_rect()
        return screen_rect.width // self.cols
    
    def tile_height(self):
        screen_rect = screen().get_rect()
        return screen_rect.height // self.rows
    
    def locationAt(self, x_index, y_index):
        x_location = self.tile_width() * x_index
        y_location = self.tile_height() * y_index
        return (x_location, y_location)
