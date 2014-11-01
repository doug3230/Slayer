'''
Created on Oct 18, 2014

@author: Richard
'''
import pygame

class LevelImages:
    WALL = None
    FLOOR = None
    LADDER = None
    MONSTER = None
    
    @staticmethod
    def initialize_images():
        from game import load_image
        LevelImages.WALL = load_image("wall.gif")
        LevelImages.FLOOR = load_image("floor.gif")
        LevelImages.LADDER = load_image("ladder.gif")
        LevelImages.MONSTER = load_image("monster.gif")
        LevelImages.resize_images()
        return
    
    @staticmethod
    def resize_images():
        from game import screen_grid, resize_image
        screen_grid = screen_grid()
        LevelImages.WALL = resize_image(LevelImages.WALL, screen_grid.tile_width(), screen_grid.tile_height())
        LevelImages.FLOOR = resize_image(LevelImages.FLOOR, screen_grid.tile_width(), screen_grid.tile_height())
        LevelImages.LADDER = resize_image(LevelImages.LADDER, screen_grid.tile_width(), screen_grid.tile_height())
        LevelImages.MONSTER = resize_image(LevelImages.MONSTER, screen_grid.tile_width(), screen_grid.tile_height())
        return

class Level:
    def __init__(self, file_name):
        from game import path_to_level
        file_handle = open(path_to_level(file_name), "r")
        line = file_handle.readline().strip()
        self.rows = int(line.split("=")[1])
        line = file_handle.readline().strip()
        self.cols = int(line.split("=")[1])
        self.elements = []
        self.ladder_indices = []
        self.ladder_links = {}
        
        line = file_handle.readline().rstrip()
        for r in range(self.rows):
            new_row = []
            for c in range(self.cols):
                if c >= len(line):
                    new_row.append(None)
                else:
                    if line[c] == "L":
                        self.ladder_indices.append((c, r))
                    new_row.append(line[c])
            self.elements.append(new_row)
            line = file_handle.readline().rstrip()
        file_handle.close()
        
        if self.ladder_indices != []:
            link_handle = open(path_to_level(file_name[:-4] + "_links.txt"))
            ladder_number = 0
            for line in link_handle:
                self.ladder_links[self.ladder_indices[ladder_number]] = line.strip()
                ladder_number += 1
            link_handle.close() 
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
        elif element == "L":
            image = LevelImages.LADDER
        elif element == "M":
            image = LevelImages.MONSTER
        return image
    
    def ladder_index(self, ladder_number):
        if not (0 <= ladder_number < len(self.ladder_indices)):
            return None
        return self.ladder_indices[ladder_number]
        
    def blitToScreen(self, x_loc, y_loc):
        from game import screen, screen_grid
        screen_grid = screen_grid()
        screen_rows = screen_grid.rows
        screen_cols = screen_grid.cols
        rows_to_top = screen_rows // 2
        cols_to_left = screen_cols // 2
        
        top_left_x = x_loc - cols_to_left
        top_left_y = y_loc - rows_to_top
        image_x = 0
        image_y = 0
        
        screen = screen()
        for x_index in range(screen_cols):
            image_y = 0
            for y_index in range(screen_rows):
                image = self.imageAt(top_left_x + x_index, top_left_y + y_index)
                if image != None:
                    screen.blit(image, (image_x, image_y))
                image_y += screen_grid.tile_height()
            image_x += screen_grid.tile_width()
        return
    
    def isWall(self, x_index, y_index):
        if self.imageAt(x_index, y_index) == None:
            return False
        return self.elements[y_index][x_index] == "W"
    
    def isLadder(self, x_index, y_index):
        if self.imageAt(x_index, y_index) == None:
            return False
        return self.elements[y_index][x_index] == "L"
    
    def isMonster(self, x_index, y_index):
        if self.imageAt(x_index, y_index) == None:
            return False
        return self.elements[y_index][x_index] == "M"
    
    def linkAt(self, x_index, y_index):
        info = self.ladder_links[(x_index, y_index)]
        link = info.split(",")
        return link
    
    def load_level(self, x_index, y_index):
        from game import Overworld
        link = self.linkAt(x_index, y_index)
        level_name = link[0]
        level = Level(level_name)
        location = level.ladder_index(int(link[1]))
        Overworld.set_center_x_index(location[0])
        Overworld.set_center_y_index(location[1])
        return level
