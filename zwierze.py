from organizm import Organizm
from random import randint

class Zwierze(Organizm):
    def __init__(self, x, y, world):
        super().__init__(x, y, world)
        self.sila = 1
        self.inicjatywa = 1
        self.color = 'purple'

    def akcja(self):
        self.age += 1
        dx = randint(-1, 1)
        dy = randint(-1, 1)

        new_x = self.x + dx
        new_y = self.y + dy

        if (new_x >= 0 and new_x < self.world.width and new_y >= 0 and new_y < self.world.height):
            self.x += dx
            self.y += dy

    def kolizja(self, other):
        if (self.sila > other.sila):
            self.world.remove_organism(other)
            return True
        elif (self.sila < other.sila):
            self.world.remove_organism(self)
            return False
        else:
            return False