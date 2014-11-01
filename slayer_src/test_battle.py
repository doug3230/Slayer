'''
Created on Oct 25, 2014

@author: Richard
'''
import pygame, game
from battle import *
from random import choice

pygame.init()
game.initialize()
pygame.display.quit()
game.load_music("ff4.wav")
game.play_music()

weapons = [ShortSword(), LongBow(), Hadouken()]
ray = Ray(weapons)
ray = ray.battle_unit()
enemies = [Skeleton(), EvilSpirit(), Dragon()]
ray_weapons = ray.weapons()
prompt = "Choose a weapon: "
for i in range(len(ray_weapons)):
    prompt += "\n{0} = {1}".format(i + 1, ray_weapons[i].name)
prompt += "\n-> "

enemy = None
enemy_weapons = None

while ray.is_alive() and (enemy != None or enemies != []):
    if enemy == None:
        enemy = enemies.pop(0)
        enemy_weapons = enemy.weapons()
        print("{0} appeared!".format(enemy.name))
    print("Ray: {0}HP, {1}: {2}HP".format(ray.HP(), enemy.name, enemy.HP()))
    ray_choice = input(prompt)
    weapon = ray_weapons[ray_choice - 1]
    raw_input("Ray attacks with {0}".format(weapon.name))
    hit, damage = weapon.attack(enemy)
    if hit:
        enemy.take_damage(damage)
        raw_input("{0} takes {1} damage!".format(enemy.name, damage))
    else:
        raw_input("Ray misses")
    
    if enemy.is_alive():
        enemy_weapon = choice(enemy_weapons)
        raw_input("{0} attacks with {1}".format(enemy.name, enemy_weapon.name))
        hit, damage = enemy_weapon.attack(enemy)
        if hit:
            ray.take_damage(damage)
            raw_input("Ray takes {0} damage!".format(damage))
        else:
            raw_input("{0} misses".format(enemy.name))
    else:
        raw_input("{0} is defeated".format(enemy.name))
        enemy = None

if ray.is_alive():
    print("You have won!")
    game.load_music("ff7.wav")
    game.play_music(False)
    raw_input()
else:
    print("Oh dear, you are dead!")
game.stop_music()