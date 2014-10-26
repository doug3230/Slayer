'''
Created on Oct 26, 2014

@author: Richard
'''
import pygame
from elements import TileElement, TileSprite

class OverworldTileElement(TileElement):
    def __init__(self, *args):
        TileElement.__init__(self, *args)
        return
    
    def update(self):
        from game import screen_grid, Overworld
        TileElement.update(self)
        screen_x_index = self.x_index - Overworld.cur_x_index
        screen_y_index = self.y_index - Overworld.cur_y_index
        self.location = screen_grid().locationAt(screen_x_index, screen_y_index)
        return
    
class OverworldTileSprite(OverworldTileElement, TileSprite, pygame.sprite.Sprite):
    def __init__(self, image_file, *args):
        OverworldTileElement.__init__(self, *args)
        TileSprite.__init__(self, image_file, *args)
        return

    def update(self, *args):
        OverworldTileElement.update(self)
        TileSprite.update(self, *args)
        return
