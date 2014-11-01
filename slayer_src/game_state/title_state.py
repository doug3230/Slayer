'''
Created on Oct 26, 2014

@author: Richard
'''
import pygame, game
from state import State
from game_sprites.title_sprites import shapes, sprites, sword

class TitleState(State):
    def __init__(self):
        State.__init__(self)
        self._shapes = shapes()
        self._sprites = sprites()
        self._sword = sword()
        self._sword_top_index = self._sword.y_index
        self._number_of_choices = 2
        self._current_choice = 0 
        return
    
    def handle_event(self, event):
        State.handle_event(self, event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                if self._current_choice < self._number_of_choices - 1:
                    self._current_choice += 1
                    self.refresh_screen = True
            elif event.key == pygame.K_UP:
                if self._current_choice > 0:
                    self._current_choice -= 1
                    self.refresh_screen = True
            elif event.key == pygame.K_RETURN:
                if self._current_choice == 0:
                    from level_state import LevelState
                    from game import set_state
                    state = LevelState("tower_entrance.txt")
                    set_state(state)
                    state.play_music()
        return
    
    def update(self):
        self._sword.y_index = self._sword_top_index + self._current_choice
        State.update(self)
        for shape in self._shapes:
            shape.update()
        self._sprites.update()
        return
    
    def draw_to_screen(self):
        State.draw_to_screen(self)
        screen = game.screen()
        for shape in self._shapes:
            shape.draw_to_screen(screen)
        self._sprites.draw(screen)
        return
    
    def play_music(self):
        from game import load_music, play_music
        load_music("ff4.wav")
        play_music()
        return
