'''
Created on Oct 26, 2014

@author: Richard
'''
from game import load_system_font
from elements import TileSprite
from elements.shapes import full_screen_rectangle, TextBox
from constants.colours import BLACK, WHITE, RED
from pygame.sprite import RenderPlain

class Private:
    SWORD = None

def sword():
    if Private.SWORD == None:
        Private.SWORD = SwordSprite()
    return Private.SWORD

def shapes():
    return [BackgroundRect(), HeaderText(), NewGameText(), LoadGameText()]

def sprites():
    return RenderPlain(sword())

def BackgroundRect():
    return full_screen_rectangle(colour=WHITE, background_colour=BLACK, thickness=10)

class HeaderText(TextBox):
    def __init__(self):
        header_font = load_system_font("Algerian", 155, bold=True)
        TextBox.__init__(self, font=header_font, text="SLAYER", font_colour=BLACK, \
                         x_index=1, y_index=2, x_tiles=8, y_tiles=3, border_tiles=0.2)
        return

class LogoSprite(TileSprite):
    def __init__(self):
        TileSprite.__init__(self, "asch2.gif", x_index=0.05, y_index=3.5, x_tiles=3.95, y_tiles=6.4)
        return

class SwordSprite(TileSprite):
    def __init__(self):
        TileSprite.__init__(self, "sword.gif", x_index=2, y_index=5, x_tiles=1.75, y_tiles=1)
        return

class NewGameText(TextBox):
    def __init__(self):
        text_font = load_system_font("Courier", 50, bold=True)
        TextBox.__init__(self, font=text_font, text="New Game", font_colour=RED, \
                         x_index=3.75, y_index=5, x_tiles=3, y_tiles=1, border_tiles=0.2)
        return
    
class LoadGameText(TextBox):
    def __init__(self):
        text_font = load_system_font("Courier", 50, bold=True)
        TextBox.__init__(self, font=text_font, text="Load Game", font_colour=RED, \
                         x_index=3.75, y_index=6, x_tiles=3.5, y_tiles=1, border_tiles=0.2)
        return

