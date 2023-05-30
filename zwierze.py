from organizm import Organizm
from random import randint


class Zwierze(Organizm):
    def __init__(self, x, y, world):
        super().__init__(x, y, world)
        self.wech = False

    def akcja(self):
        self.age += 1
        dx = randint(-1, 1)
        dy = randint(-1, 1)

        new_x = self.x + dx
        new_y = self.y + dy

        if (new_x >= 0 and new_x < self.world.width and new_y >= 0 and new_y < self.world.height):
            if (not self.world.is_ocuppied(new_x, new_y)):
                self.x = new_x
                self.y = new_y
            elif (not self.wech):
                self.world.get_organism(new_x, new_y).kolizja(self)

    def kolizja(self, other):
        if (self.__class__ == other.__class__):
            if self.age < 10 or other.age < 10:
                return
            new_x = self.x
            new_y = self.y
            while (new_x == self.x and new_y == self.y):
                new_x = self.x + randint(-1, 1)
                new_y = self.y + randint(-1, 1)
                if (new_x >= 0 and new_x < self.world.width and new_y >= 0 and new_y < self.world.height):
                    if (not self.world.is_ocuppied(new_x, new_y)):
                        self.world.add_organism(self.__class__.__name__, new_x, new_y)
                        print(self.__class__.__name__, "rozmnozyl sie")
                        return True
            return False
        if (self.sila <= other.sila):
            other.x = self.x
            other.y = self.y
            self.world.remove_organism(self)
            print(self.__class__.__name__, "zostal zabity przez", other.__class__.__name__)
        else:
            other.world.remove_organism(other)
            print(other.__class__.__name__, "zostal zabity przez", self.__class__.__name__)
