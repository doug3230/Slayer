'''
Created on Oct 18, 2014

@author: Richard
'''
import pygame, game

class TileSprite(pygame.sprite.Sprite):
    def __init__(self, image_file, x_index = 0, y_index = 0, x_tiles = 1, y_tiles = 1):
        pygame.sprite.Sprite.__init__(self)
        self.x_index = x_index
        self.y_index = y_index
        self.x_tiles = x_tiles
        self.y_tiles = y_tiles
        self.image = game.load_image(image_file)
        self.update_size()
        self.update()
        return
    
    def width(self):
        return game.screen_grid().tile_width * self.x_tiles
    
    def height(self):
        return game.screen_grid().tile_height * self.y_tiles
    
    def update(self, *args):
        pygame.sprite.Sprite.update(self, *args)
        screen_grid = game.screen_grid()
        screen_x_index = self.x_index - game.Location.cur_x_index
        screen_y_index = self.y_index - game.Location.cur_y_index
        location = screen_grid.locationAt(screen_x_index, screen_y_index)
        self.rect = pygame.Rect(location, (self.width(), self.height()))
        return
    
    def update_size(self):
        self.image = game.resize_image(self.image, self.width(), self.height())
        self.image.convert()
        return
