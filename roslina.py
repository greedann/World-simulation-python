from organizm import Organizm

import random

class Roslina(Organizm):
    def __init__(self, x, y, world):
        super().__init__(x, y, world)
        self.sila = 0
        self.inicjatywa = 0
        self.nazwa = "Roslina"
        self.color = 'green'


    def akcja(self):
        self.age += 1
        if (random.randint(0, 100) < 20):
            new_x = self.x+random.randint(-1, 1)
            new_y = self.y+random.randint(-1, 1)
            if (new_x >= 0 and new_x < self.world.width and new_y >= 0 and new_y < self.world.height):
                self.world.add_organism(self.nazwa, new_x, new_y)

    def kolizja(self, other):
        other.x = self.x
        other.y = self.y
        self.world.remove_organism(self)
