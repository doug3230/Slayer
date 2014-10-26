'''
Created on Oct 18, 2014

@author: Richard
'''
from overworld import OverworldTileSprite

class Ray(OverworldTileSprite):
    def __init__(self):
        from game import Overworld
        OverworldTileSprite.__init__(self, "ray.gif", Overworld.center_x_index(), Overworld.center_y_index(), 1, 1)
        return
