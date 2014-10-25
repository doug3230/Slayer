'''
Created on Oct 12, 2014

@author: Richard
'''
import pygame, game, game_state

game.initialize()
screen = game.screen()
screen_grid = game.screen_grid()
game.Location.set_center_x_index(1)
game.Location.set_center_y_index(1)
state = game_state.LevelState("tower_entrance.txt")
state.draw_to_screen()
pygame.display.flip()

game.load_music("travelers.mp3")
game.play_music()

while True:
    screen.fill(game.background())
    for event in pygame.event.get():
        state.handle_event(event)
    state.update()
    state.draw_to_screen()
    if state.update_screen:
        pygame.display.flip()
        state.update_screen = False
    state = state.current_game_state
    game.tick()
