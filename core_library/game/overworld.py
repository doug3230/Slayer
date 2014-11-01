'''
Created on Oct 18, 2014

@author: Richard
'''
import game

class Overworld:
    cur_x_index = 0
    cur_y_index = 0
    
    @staticmethod
    def center_x_index():
        screen_grid = game.components.screen_grid()
        return Overworld.cur_x_index + screen_grid.cols // 2
    
    @staticmethod
    def center_y_index():
        screen_grid = game.components.screen_grid()
        return Overworld.cur_y_index + screen_grid.rows // 2
    
    @staticmethod
    def set_center_x_index(x_index):
        screen_grid = game.components.screen_grid()
        Overworld.cur_x_index = x_index - screen_grid.cols // 2
        return
        
    @staticmethod
    def set_center_y_index(y_index):
        screen_grid = game.components.screen_grid()
        Overworld.cur_y_index = y_index - screen_grid.rows // 2
        return
