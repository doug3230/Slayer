'''
Created on Oct 25, 2014

@author: Richard
'''
from unit import Unit
from melee import *
from magic import *

class Skeleton(Unit):
    def __init__(self):
        WEAPONS = [ShortSword(self)]
        Unit.__init__(self, "Skeleton", HP = 50, ATK = 10, DEF = 6, ACC = 7, EVA = 9, SPD = 5, weapons = WEAPONS)
        return

class EvilSpirit(Unit):
    def __init__(self):
        WEAPONS = [ShortSword(self), BlackBlade(self)]
        Unit.__init__(self, "Evil Spirit", HP = 75, ATK = 12, DEF = 12, MAG = 0, RES = 0, ACC = 8, EVA = 8, SPD = 8, weapons = WEAPONS)
        return
    
class Dragon(Unit):
    def __init__(self):
        WEAPONS = [FireBall(self)]
        Unit.__init__(self, "Dragon", HP = 9999, ATK = 9999, DEF = 9999, MAG = 9999, RES = 9999, ACC = 9999, EVA = 9999, SPD = 9999, weapons = WEAPONS)
        return

