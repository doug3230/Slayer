'''
Created on Oct 25, 2014

@author: Richard
'''
import random

class Weapon:
    def __init__(self, name, type, power, owner = None, ATK = 0, DEF = 0, MAG = 0, RES = 0, ACC = 0, EVA = 0, SPD = 0):
        self.name = name
        self.owner = owner
        self.power = power
        self._type = type
        self.ATK = ATK
        self.DEF = DEF
        self.MAG = MAG
        self.RES = RES
        self.ACC = ACC
        self.EVA = EVA
        self.SPD = SPD
        return
    
    def is_melee(self):
        return self._type == "Melee"

    def is_magic(self):
        return self._type == "Magic"
    
    def attack(self, target):
        def melee_attack(target):
            acc_dif = self.owner.ACC() - target.EVA()
            acc_bonus = acc_dif * 0.1
            hit = random.random() < 0.5 + acc_bonus
            damage = 0
            
            if hit:    
                atk_dif = self.owner.ATK() - target.DEF()
                atk_bonus = atk_dif * 0.1
                damage = int(self.power * (1 + atk_bonus))
                damage = max(damage, 0)
            return hit, damage
        
        def magic_attack(target):
            mag_dif = self.owner.MAG() - target.RES()
            mag_bonus = mag_dif * 0.1
            damage = int(self.power * (1 + mag_bonus))
            damage = max(damage, 0)
            return True, damage
        
        self.owner.active_weapon = self
        if self.is_melee():
            return melee_attack(target)
        else:
            return magic_attack(target)
    
class MeleeWeapon(Weapon):
    def __init__(self, name,  power, owner = None, ATK = 0, DEF = 0, ACC = 0, EVA = 0, SPD = 0):
        Weapon.__init__(self, name, "Melee", power, owner, ATK, DEF, 0, 0, ACC, EVA, SPD)
        return
    
class MagicWeapon(Weapon):
    def __init__(self, name, power, owner = None, MAG = 0, RES = 0, SPD = 0):
        Weapon.__init__(self, name, "Magic", power, owner, 0, 0, MAG, RES, 0, 0, SPD)
        return
