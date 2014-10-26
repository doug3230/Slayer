'''
Created on Oct 25, 2014

@author: Richard
'''
from weapon import MeleeWeapon

class ShortSword(MeleeWeapon):
    def __init__(self, owner = None):
        MeleeWeapon.__init__(self, "ShortSword", 8, owner, ATK = 2, DEF = 1)
        return
    
class LongBow(MeleeWeapon):
    def __init__(self, owner = None):
        MeleeWeapon.__init__(self, "LongBow", 8, owner, DEF = 1, ACC = 4)
        return

class BlackBlade(MeleeWeapon):
    def __init__(self, owner = None):
        MeleeWeapon.__init__(self, "BlackBlade", 12, owner, ATK = 3, DEF = 2, ACC = 2)
        return
