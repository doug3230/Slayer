'''
Created on Oct 18, 2014

@author: Richard
'''
import core
from game import Location

class Ray(core.TileSprite):
    def __init__(self):
        core.TileSprite.__init__(self, "ray.gif", Location.center_x_index(), Location.center_y_index(), 1, 1)
        return
    
    def update(self, *args):
        self.x_index = Location.center_x_index()
        self.y_index = Location.center_y_index()
        core.TileSprite.update(self, *args)
        return
