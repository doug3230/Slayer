'''
Created on Oct 25, 2014

@author: Richard
'''
from battle.unit import PlayerUnit

class Character:
    def __init__(self, name, hitpoints = 100, level = 1, STR = 0, DEX = 0, SOR = 0, weapons = []):
        self.name = name
        self.hitpoints = hitpoints
        self.level = level
        self.STR = STR
        self.DEX = DEX
        self.SOR = SOR
        self.weapons = weapons
        return
    
    def max_hitpoints(self):
        return self.level * 100
    
    def base_atk(self):
        return (self.STR)
    
    def base_def(self):
        return (self.STR + self.DEX) // 2
    
    def base_mag(self):
        return (self.SOR)
    
    def base_res(self):
        return (self.SOR + self.DEX) // 2
    
    def base_acc(self):
        return (self.DEX)
    
    def base_eva(self):
        return (self.DEX * 3 + self.STR) // 4
    
    def base_spd(self):
        return (self.DEX * 3 + self.SOR) // 4

    def battle_unit(self):
        return PlayerUnit(self)
