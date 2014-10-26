'''
Created on Oct 18, 2014

@author: Richard
'''
import pygame

class TileElement:
    def __init__(self, x_index = 0, y_index = 0, x_tiles = 1, y_tiles = 1):
        self.x_index = x_index
        self.y_index = y_index
        self.x_tiles = x_tiles
        self.y_tiles = y_tiles
        self.update()
        return
    
    def width(self):
        from game import screen_grid
        return screen_grid().tile_width * self.x_tiles
    
    def height(self):
        from game import screen_grid
        return screen_grid().tile_height * self.y_tiles
    
    def update(self):
        from game import screen_grid
        self.location = screen_grid().locationAt(self.x_index, self.y_index)
        return

class TileShape(TileElement):
    def __init__(self, *args):
        TileElement.__init__(self, *args)
        return
    
    def draw_to_screen(self, screen):
        return
    
    def update(self):
        TileElement.update(self)
        return

class TileSprite(TileElement, pygame.sprite.Sprite):
    def __init__(self, image_file, *args):
        from game import load_image
        TileElement.__init__(self, *args)
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image(image_file)
        self.update_size()
        self.update()
        return
    
    def update(self, *args):
        pygame.sprite.Sprite.update(self, *args)
        TileElement.update(self)
        self.rect = pygame.Rect(self.location, (self.width(), self.height()))
        return
    
    def update_size(self):
        from game import resize_image
        self.image = resize_image(self.image, self.width(), self.height())
        self.image.convert()
        return

