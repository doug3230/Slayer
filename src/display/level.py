'''
Created on Oct 18, 2014

@author: Richard
'''
import pygame, game

class LevelImages:
    WALL = None
    FLOOR = None
    
    @staticmethod
    def initialize_images():
        LevelImages.WALL = game.load_image("wall.gif")
        LevelImages.FLOOR = game.load_image("floor.gif")
        LevelImages.resize_images()
        return
    
    @staticmethod
    def resize_images():
        screen_grid = game.screen_grid()
        LevelImages.WALL = game.resize_image(LevelImages.WALL, screen_grid.tile_width, screen_grid.tile_height)
        LevelImages.FLOOR = game.resize_image(LevelImages.FLOOR, screen_grid.tile_width, screen_grid.tile_height)
        return

class Level:
    def __init__(self, file_name):
        file_handle = open(game.path_to_level(file_name), "r")
        line = file_handle.readline().strip()
        self.rows = int(line.split("=")[1])
        line = file_handle.readline().strip()
        self.cols = int(line.split("=")[1])
        self.elements = []
        
        line = file_handle.readline().strip()
        while line != "":
            new_row = []
            for char in line:
                new_row.append(char)
            self.elements.append(new_row)
            line = file_handle.readline().strip()
        file_handle.close()
        return
    
    def imageAt(self, x_index, y_index):
        if not (0 <= x_index < self.cols and 0 <= y_index < self.rows):
            return None
        element = self.elements[y_index][x_index]
        image = None
        if element == "W":
            image = LevelImages.WALL
        elif element == "F":
            image = LevelImages.FLOOR
        return image
        
    def blitToScreen(self, x_loc, y_loc):
        screen_grid = game.screen_grid()
        screen_rows = screen_grid.rows
        screen_cols = screen_grid.cols
        rows_to_top = screen_rows // 2
        cols_to_left = screen_cols // 2
        
        top_left_x = x_loc - cols_to_left
        top_left_y = y_loc - rows_to_top
        image_x = 0
        image_y = 0
        
        screen = game.screen()
        for x_index in range(screen_cols):
            image_y = 0
            for y_index in range(screen_rows):
                image = self.imageAt(top_left_x + x_index, top_left_y + y_index)
                if image != None:
                    screen.blit(image, (image_x, image_y))
                image_y += screen_grid.tile_height
            image_x += screen_grid.tile_width
        return
