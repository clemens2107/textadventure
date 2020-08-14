# -*- coding: utf-8 -*-
import random
from items.consumables.potions.potions import potion_list

drop_list = []
item_list = [potion_list]

# roll droop changs and loot
def loot():
    rand = 1 #random.randint(0,2)
    item_quantity = random.randint(0,3)
    if rand == 1:
        for i in range(item_quantity):
            item_category = item_list[random.randint(0, len(item_list) - 1)]
            item_under_category = item_category[random.randint(0, len(item_category) - 1)]
            item = item_under_category[random.randint(0, len(item_under_category)- 1)]
            drop_list.append(item)

class Item:
    def __init__(self, level, name, weight, worth):
        self.level = level
        self.name = name
        self.weight = weight
        self.worth = worth