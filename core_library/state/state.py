'''
Created on Oct 23, 2014

@author: Richard
'''
import pygame, game

class State:
    def __init__(self, music_file = None):
        self.refresh_screen = True
        self.music_file = music_file
        return
    
    def handle_event(self, event):
        if event.type == pygame.locals.QUIT:
            game.finalization.finalize()
        return
    
    def update(self):
        return
    
    def draw_to_screen(self):
        screen = game.components.screen()
        background = game.components.background()
        screen.fill(background)
        return
    
    def play_music(self):
        if self.music_file:
            game.file_processing.load_music(self.music_file)
            game.file_processing.play_music()
        return
    
class ResizingState(State):
    def handle_event(self, event):
        State.handle_event(self, event)
        if event.type == pygame.locals.VIDEORESIZE:
            game.resize_screen(event.dict['size'])
            self.resize_elements()
            self.refresh_screen = True
        return
    
    def resize_elements(self):
        return
    
