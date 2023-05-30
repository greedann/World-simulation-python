from zwierze import Zwierze

import random

class Antylopa(Zwierze):
    def __init__(self, x, y, world):
        super().__init__(x, y, world)
        self.sila = 4
        self.inicjatywa = 4
        self.color = "cyan"

    def akcja(self):
        for _ in range(2):
            super().akcja()

    def kolizja(self, other):
        dice = random.randint(0, 1)
        if (dice == 0 and other.__class__.__name__ ==self.__class__.__name__):
            super().kolizja(other)
        else:
            new_pos = self.world.find_free_neardy(self.x, self.y)
            if new_pos is not None:
                self.x = new_pos[0]
                self.y = new_pos[1]
                print("Antylopa uciekła")
            else:
                super().kolizja(other)
        