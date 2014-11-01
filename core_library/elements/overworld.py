'''
Created on Oct 26, 2014

@author: Richard
'''
import game
from elements import TileElement, TileShape, TileSprite

class OverworldTileElement(TileElement):
    def update(self):
        TileElement.update(self)
        screen_x_index = self.x_index - game.Overworld.cur_x_index
        screen_y_index = self.y_index - game.Overworld.cur_y_index
        screen_grid = game.screen_grid()
        self.location = screen_grid.locationAt(screen_x_index, screen_y_index)
        return
    
class OverworldTileShape(OverworldTileElement, TileShape):
    pass
    
class OverworldTileSprite(OverworldTileElement, TileSprite):
    def __init__(self, image_file, *args, **kwargs):
        OverworldTileElement.__init__(self, *args, **kwargs)
        TileSprite.__init__(self, image_file, *args, **kwargs)
        return

    def update(self, *args):
        OverworldTileElement.update(self)
        TileSprite.update(self, *args)
        return
