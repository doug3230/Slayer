'''
Created on Oct 26, 2014

@author: Richard
'''
from elements import TileSprite

class HeaderSprite(TileSprite):
    def __init__(self, x_index = 1, y_index = 0.5, x_tiles = 8, y_tiles = 3):
        TileSprite.__init__(self, "title.gif", x_index, y_index, x_tiles, y_tiles)
        return

class LogoSprite(TileSprite):
    def __init__(self, x_index = 0.1, y_index = 3.5, x_tiles = 3.9, y_tiles = 6.4):
        TileSprite.__init__(self, "asch.gif", x_index, y_index, x_tiles, y_tiles)
        return

class SwordSprite(TileSprite):
    def __init__(self, x_index = 4.25, y_index = 5, x_tiles = 1.75, y_tiles = 1):
        TileSprite.__init__(self, "sword.gif", x_index, y_index, x_tiles, y_tiles)
        return
    
class NewGameSprite(TileSprite):
    def __init__(self, x_index = 6, y_index = 5, x_tiles = 3, y_tiles = 1):
        TileSprite.__init__(self, "new_game.gif", x_index, y_index, x_tiles, y_tiles)
        return
    
class LoadGameSprite(TileSprite):
    def __init__(self, x_index = 6, y_index = 6, x_tiles = 3.5, y_tiles = 1):
        TileSprite.__init__(self, "load_game.gif", x_index, y_index, x_tiles, y_tiles)
        return
