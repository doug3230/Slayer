'''
Created on Oct 27, 2014

@author: Richard
'''
import pygame, game

def main(initial_state = None):
    game.initialize()
    if initial_state:
        game.set_state(initial_state)
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
    return

if __name__ == "__main__":
    main()
