'''
Created on Oct 23, 2014

@author: Richard
'''
import pygame, game

class State:
    def __init__(self):
        self.refresh_screen = True
        return
    
    def handle_event(self, event):
        from pygame.locals import QUIT
        if event.type == QUIT:
            from game import stop_music
            from sys import exit
            stop_music()
            pygame.quit()
            exit()
        return
    
    def update(self):
        return
    
    def draw_to_screen(self, screen = game.screen()):
        from game import background
        screen.fill(background())
        return
    
    def play_music(self):
        return
