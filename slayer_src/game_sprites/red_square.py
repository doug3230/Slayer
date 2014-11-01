'''
Created on Oct 30, 2014

@author: Richard
'''
import pygame
from elements import OverworldTileShape

class RedSquare(OverworldTileShape):
    def draw_to_screen(self, screen):
        OverworldTileShape.draw_to_screen(self, screen)
        location = self.location
        size = (self.width(), self.height())
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(location, size))
        return
    