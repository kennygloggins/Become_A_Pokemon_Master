# By: Kenny_G_Loggins
# Created on: 7/19/20, 10:51 PM
# File: pokemon_master.py
# Project: Become_A_Pokemon_Master

import sys, os

# Disable
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore
def enablePrint():
    sys.stdout = sys.__stdout__

# POKE_ID = 0

class Pokemon:

    element = {'strong': {'water': 'fire', 'fire': 'grass', 'grass': 'water'},
               'weak': {'water': 'grass', 'fire':'water','grass': 'fire'}}

    # POKE_ID += 1

    def __init__(self, name, level, ptype, max_hp, c_hp, knocked):
        self.name = name
        self.level = level
        self.ptype = ptype
        self.max_hp = max_hp
        self.c_hp = c_hp
        self.knocked = knocked
        # self.poken_pokei = {POKE_ID: [self.name, self.level, self.ptype, self.max_hp, self.c_hp, self.knocked}

    def lose_heatlh(self, minus_hp):
        if self.c_hp - minus_hp <= 0:
            self.c_hp = 0
            return self.knock_out()
        else:
            self.c_hp -= minus_hp
            print('{} now has {} health'.format(self.name, self.c_hp))

    def gain_health(self, plus_hp):
        self.c_hp += plus_hp
        print('{} now has {} health'.format(self.name, self.c_hp))

    def knock_out(self):
        if self.c_hp == 0:
            self.knocked = True
            print('{} has been knocked out'.format(self.name))
        else:
            self.knocked = False


    def revive(self):
        if self.knocked:
            self.c_hp = self.max_hp * .5
        else:
            return 'Can\'t do this yet. {} is not knocked.'.format(self.name)

    def attack(self, Pokemon, dmg):
        norm = True
        for ele in self.element['strong']:
            if ele == self.ptype and  self.element['strong'][ele] == Pokemon.ptype:
                crit = dmg * 2
                norm = False
                print('Critical STRIKE! {} took {} damage'.format(Pokemon.name, crit))
                Pokemon.lose_heatlh(crit)
        for ele in self.element['weak']:
            if ele == self.ptype and self.element['weak'][ele] == Pokemon.ptype:
                wiff = dmg / 2
                norm = False
                print('Was not very effective. {} took {} damage'.format(Pokemon.name, wiff))
                Pokemon.lose_heatlh(wiff)

        if norm:
            return '{} took {} damage'.format(Pokemon.name, dmg), Pokemon.lose_heatlh(dmg)



class Trainer:
    def __init__(self, lst_pokemon, name, n_potions, active_pok):
        self.lst_pokemon = lst_pokemon
        self.name = name
        self.n_potions = n_potions
        self.active_pok = active_pok

    def use_potion(self, Pokemon):
        if self.n_potions > 0:
            Pokemon.gain_health(10)
            self.n_potions -= 1
        else:
            print('You have no potions!')


    def attack(self, Trainer, dmg):
        self.active_pok.attack(Trainer.active_pok, dmg)


charmander = Pokemon('Charmander', 12, 'fire', 32, 32, False)
squirtle = Pokemon('Squirtle', 12, 'water', 32, 32, False)
charmander2 = Pokemon('Charmander', 12, 'fire', 32, 32, False)

squirtle.attack(charmander2, 4)
squirtle.attack(charmander2, 4)
squirtle.attack(charmander2, 4)
squirtle.attack(charmander2, 4)
# print(charmander2.c_hp)
