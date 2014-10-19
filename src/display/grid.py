'''
Created on Oct 18, 2014

@author: Richard
'''
import game

class ScreenGrid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        screen_rect = game.screen().get_rect()
        self.tile_width = screen_rect.width // self.cols
        self.tile_height = screen_rect.height // self.rows
        return
    
    def locationAt(self, x_index, y_index):
        screen_rect = game.screen().get_rect()
        self.tile_width = screen_rect.width // self.cols
        self.tile_height = screen_rect.height // self.rows
        x_location = self.tile_width * x_index
        y_location = self.tile_height * y_index
        return (x_location, y_location)
