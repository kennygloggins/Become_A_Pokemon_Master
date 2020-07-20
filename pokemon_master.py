# By: Kenny_G_Loggins
# Created on: 7/19/20, 10:51 PM
# File: pokemon_master.py
# Project: Become_A_Pokemon_Master


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
        # self.poken_pokei = {self.name: POKE_ID}

    def lose_heatlh(self, minus_hp):
        if self.c_hp - minus_hp < 0:
            self.c_hp = 0
        else:
            self.c_hp -= minus_hp
        return '{} now has {} health'.format(self.name, self.c_hp)

    def gain_health(self, plus_hp):
        self.c_hp += plus_hp
        return '{} now has {} health'.format(self.name, self.c_hp)

    def knock_out(self):
        if self.c_hp == 0:
            self.knocked = True
        else:
            self.knocked = False
        if self.knocked:
            return '{} has been knocked out'.format(self.name)

    def revive(self): # todo finish revive method
        pass

    def attack(self, Pokemon, dmg):
        norm = True
        for ele in self.element['strong']:
            if ele == self.ptype and  self.element['strong'][ele] == Pokemon.ptype:
                crit = dmg * 2
                Pokemon.lose_heatlh(crit)
                norm = False
                return 'Critical STRIKE! {} took {} damage'.format(Pokemon.name, crit)
        for ele in self.element['weak']:
            if ele == self.ptype and self.element['weak'][ele] == Pokemon.ptype:
                wiff = dmg / 2
                Pokemon.lose_heatlh(wiff)
                norm = False
                return 'Was not very effective. {} took {} damage'.format(Pokemon.name, wiff)
        if norm == True:
            Pokemon.lose_heatlh(Pokemon, dmg)
            return '{} took {} damage'.format(Pokemon.name, dmg)


class Trainer:
    def __init__(self, lst_pokemon, name, n_potions, active_pok):
        self.lst_pokemon = lst_pokemon
        self.name = name
        self.n_potions = n_potions
        self.active_pok = active_pok

    def use_potion(self): # todo find out how much to heal for and write method
        pass

    def attack(self, trainer): # todo write method
        pass


charmander = Pokemon('Charmander', 12, 'fire', 32, 32, False)
squirtle = Pokemon('Squirtle', 12, 'water', 32, 32, False)

print(squirtle.attack(charmander, 4))