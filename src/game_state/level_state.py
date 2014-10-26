'''
Created on Oct 26, 2014

@author: Richard
'''
import pygame, game
from state import State

class LevelState(State):
    def __init__(self, level_name):
        from display import Level, LevelImages
        from sprites import Ray
        from game import Overworld
        State.__init__(self)
        LevelImages.initialize_images()
        self._level = Level(level_name)
        ray = Ray()
        self._sprite = pygame.sprite.RenderPlain(ray)
        Overworld.set_center_x_index(1)
        Overworld.set_center_y_index(1)
        return
    
    def handle_event(self, event):
        from game import Overworld
        State.handle_event(self, event)
        if event.type == pygame.KEYDOWN:
            old_cur_x_index, old_cur_y_index = Overworld.cur_x_index, Overworld.cur_y_index
            if event.key == pygame.K_UP:
                Overworld.cur_y_index -= 1
                self.refresh_screen = True
            elif event.key == pygame.K_DOWN:
                Overworld.cur_y_index += 1
                self.refresh_screen = True
            elif event.key == pygame.K_LEFT:
                Overworld.cur_x_index -= 1
                self.refresh_screen = True
            elif event.key == pygame.K_RIGHT:
                Overworld.cur_x_index += 1
                self.refresh_screen = True
            if self._level.isWall(Overworld.center_x_index(), Overworld.center_y_index()):
                Overworld.cur_x_index = old_cur_x_index
                Overworld.cur_y_index = old_cur_y_index
            elif self._level.isLadder(Overworld.center_x_index(), Overworld.center_y_index()):
                self._level = self._level.load_level(Overworld.center_x_index(), Overworld.center_y_index())
                self.refresh_screen = True
            elif self._level.isMonster(Overworld.center_x_index(), Overworld.center_y_index()):
                from game import set_state
                from battle_state import BattleState
                from battle import Skeleton
                new_state = BattleState(Skeleton())
                set_state(new_state)
                new_state.play_music()
        return
    
    def draw_to_screen(self, screen = game.screen()):
        from game import Overworld
        State.draw_to_screen(self, screen)
        self._level.blitToScreen(Overworld.center_x_index(), Overworld.center_y_index())
        self._sprite.draw(screen)
        return
    
    def update(self):
        State.update(self)
        self._sprite.update()
        return
    
    def play_music(self):
        from game import load_music, play_music
        load_music("travelers.mp3")
        play_music()
        return
