'''
Created on Oct 12, 2014

@author: Richard
'''
import sys
import pygame, game, display, sprites
from pygame.locals import QUIT
from game import Location
from display import LevelImages

game.initialize()
screen = game.screen()
screen_grid = game.screen_grid()

game.load_music("travelers.mp3")
game.play_music()

LevelImages.initialize_images()
level = display.Level("tower_entrance.txt")
ray = sprites.Ray()
sprite = pygame.sprite.RenderPlain(ray)
Location.set_center_x_index(1)
Location.set_center_y_index(1)

update_screen = True
while True:
    screen.fill(game.background())
    for event in pygame.event.get():
        if event.type == QUIT:
            game.stop_music()
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            old_cur_x_index, old_cur_y_index = Location.cur_x_index, Location.cur_y_index
            update_screen = True
            if event.key == pygame.K_UP:
                Location.cur_y_index -= 1
            elif event.key == pygame.K_DOWN:
                Location.cur_y_index += 1
            elif event.key == pygame.K_LEFT:
                Location.cur_x_index -= 1
            elif event.key == pygame.K_RIGHT:
                Location.cur_x_index += 1
            else:
                update_screen = False
            if level.imageAt(Location.center_x_index(), Location.center_y_index()) == LevelImages.WALL:
                Location.cur_x_index = old_cur_x_index
                Location.cur_y_index = old_cur_y_index
                update_screen = False
    level.blitToScreen(Location.center_x_index(), Location.center_y_index())
    sprite.update()
    sprite.draw(screen)
    if update_screen:
        pygame.display.flip()
    update_screen = False
    game.tick()
