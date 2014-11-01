'''
Created on Oct 25, 2014

@author: Richard
'''
from copy import deepcopy

class Unit:
    def __init__(self, name, HP = 0, ATK = 0, DEF = 0, MAG = 0, RES = 0, ACC = 0, EVA = 0, SPD = 0, weapons = []):
        self.name = name
        self._HP = HP
        self._ATK = ATK
        self._DEF = DEF
        self._MAG = MAG
        self._RES = RES
        self._ACC = ACC
        self._EVA = EVA
        self._SPD = SPD
        self.active_weapon = None
        self._weapons = weapons
        return
    
    def HP(self):
        HP = self._HP
        return HP
    
    def ATK(self):
        ATK = self._ATK
        if self.active_weapon != None:
            ATK += self.active_weapon.ATK
        return ATK
    
    def DEF(self):
        DEF = self._DEF
        if self.active_weapon != None:
            DEF += self.active_weapon.DEF
        return DEF
    
    def MAG(self):
        MAG = self._MAG
        if self.active_weapon != None:
            MAG += self.active_weapon.MAG
        return MAG
    
    def RES(self):
        RES = self._RES
        if self.active_weapon != None:
            RES += self.active_weapon.RES
        return RES
    
    def ACC(self):
        ACC = self._ACC
        if self.active_weapon != None:
            ACC += self.active_weapon.ACC
        return ACC
    
    def EVA(self):
        EVA = self._EVA
        if self.active_weapon != None:
            EVA += self.active_weapon.EVA
        return EVA
    
    def SPD(self):
        SPD = self._SPD
        if self.active_weapon != None:
            SPD += self.active_weapon.SPD
        return SPD
    
    def weapons(self):
        return self._weapons
    
    def take_damage(self, damage):
        self._HP -= damage
        self._HP = max(self._HP, 0)
        return
    
    def is_alive(self):
        return self.HP() > 0
    
    def __str__(self):
        string = self.name + "\n"
        string += "--------------------\n"
        string += "ATK: {0}\n".format(self.ATK())
        string += "DEF: {0}\n".format(self.DEF())
        string += "MAG: {0}\n".format(self.MAG())
        string += "RES: {0}\n".format(self.RES())
        string += "ACC: {0}\n".format(self.ACC())
        string += "EVA: {0}\n".format(self.EVA())
        string += "SPD: {0}\n".format(self.SPD())
        return string

class PlayerUnit(Unit):
    def __init__(self, player_character):
        name = player_character.name
        HP = player_character.hitpoints
        ATK = player_character.base_atk()
        DEF = player_character.base_def()
        MAG = player_character.base_mag()
        RES = player_character.base_res()
        ACC = player_character.base_acc()
        EVA = player_character.base_eva()
        SPD = player_character.base_spd()
        weapons = deepcopy(player_character.weapons)
        for w in weapons:
            w.owner = self
        Unit.__init__(self, name, HP, ATK, DEF, MAG, RES, ACC, EVA, SPD, weapons)
        return
