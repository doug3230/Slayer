'''
Created on Oct 18, 2014

@author: Richard
'''
from elements import OverworldTileSprite

class Ray(OverworldTileSprite):
    def __init__(self):
        from game import Overworld
        OverworldTileSprite.__init__(self, "ray.gif", x_index=Overworld.center_x_index(), y_index=Overworld.center_y_index(), x_tiles=1, y_tiles=1)
        return
