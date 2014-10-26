'''
Created on Oct 25, 2014

@author: Richard
'''
from character import Character

class Ray(Character):
    def __init__(self, weapons = None):
        for weapon in weapons:
            weapon.owner = self
        Character.__init__(self, "Ray", STR = 12, DEX = 9, SOR = 6, weapons = weapons)
        return
