'''
Created on Oct 26, 2014

@author: Richard
'''
from state import State
import game

class BattleState(State):
    def __init__(self, monster):
        from sprites import Rectangle
        State.__init__(self)
        full_rect = Rectangle(colour = (0, 0, 0), thickness = 4, x_index = 0, y_index = 0, x_tiles = 10, y_tiles = 10)
        rect = Rectangle(colour = (0, 0, 0), thickness = 2, x_index = 0.25, y_index = 7.75, x_tiles = 9.5, y_tiles = 2)
        self._shapes = [full_rect, rect]
        return
    
    def draw_to_screen(self, screen = game.screen()):
        State.draw_to_screen(self, screen)
        screen.fill((255, 255, 255))
        for shape in self._shapes:
            shape.draw_to_screen(screen)
        return
    
    def handle_event(self, event):
        State.handle_event(self, event)
        return
    
    def update(self):
        State.update(self)
        for shape in self._shapes:
            shape.update()
        return
    
    def play_music(self):
        from game import load_music, play_music
        load_music("ff4.mp3")
        play_music()
        return
