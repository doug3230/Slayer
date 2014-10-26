'''
Created on Oct 12, 2014

@author: Richard
'''
import pygame, game

game.initialize()
state = game.state()
state.play_music()
while True:
    for event in pygame.event.get():
        state.handle_event(event)
    state.update()
    if state.refresh_screen:
        state.draw_to_screen()
        game.refresh_screen()
        state.refresh_screen = False
    state = game.state()
    game.tick()
