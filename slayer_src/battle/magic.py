'''
Created on Oct 25, 2014

@author: Richard
'''
from weapon import MagicWeapon

class FireBall(MagicWeapon):
    def __init__(self, owner = None):
        MagicWeapon.__init__(self, "FireBall", 100, owner, MAG = 9001)
        return

class Hadouken(MagicWeapon):
    def __init__(self, owner = None):
        MagicWeapon.__init__(self, "Hadouken", 9999, owner, MAG = 99999)
        return
