# -*- coding: utf-8 -*-
import enemies
import random

class field:
    def __init__(self, enemies):
        self.enemies = enemies
    
    def print_state(self):
        print("Du siehst dich um und endeckst")
        for i in self.enemies:
            print(i.name)

    @staticmethod
    def gen_random():
        rand = random.randint(1,3)
        if rand == 0:
            return field([])
        elif rand == 1:
            return field([enemies.enemie_list[random.randint(0, len(enemies.enemie_list) - 1)]])
        elif rand == 2:
            return field([enemies.enemie_list[random.randint(0, len(enemies.enemie_list) - 1)], enemies.enemie_list[random.randint(0, len(enemies.enemie_list) - 1)]])
        elif rand == 3:
            return field([enemies.enemie_list[random.randint(0, len(enemies.enemie_list) - 1)], enemies.enemie_list[random.randint(0, len(enemies.enemie_list) - 1)], enemies.enemie_list[random.randint(0, len(enemies.enemie_list) - 1)]])

class Map:
    def __init__(self, width, height):
        self.state = []
        self.x = 0
        self.y = 0
        for i in range(width):
            fields = []
            for j in range(height):
                fields.append(field.gen_random())
            self.state.append(fields)
            
    def print_state(self):
        self.state[self.x][self.y].print_state()
    
    def forward(self):
        if self.x == len(self.state) - 1:
            print("Du siehst hohe Berge und kommst nicht weiter")
        else:
            self.x = self.x + 1
            
    def backwards(self):
        if self.x == 0:
            print("Du siehst Meer und kommst nicht wieter")
        else:
            self.x = self.x + 1
            
    def right(self):
        if self.y == len(self.state[self.x]) - 1:
            print("Du siehst hohe Berge und kommst nicht weiter")
        else:
            self.y = self.y + 1
            
    def left(self):
        if self.y == 0:
            print("Du siehst Meer und kommst nicht wieter")
        else:
            self.y = self.y + 1
    
    def get_enemies(self):
        return self.state[self.x][self.y].enemies