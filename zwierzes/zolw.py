from zwierze import Zwierze

class Zolw(Zwierze):
    def __init__(self, x, y, world):
        super().__init__(x, y, world)
        self.sila = 2
        self.inicjatywa = 1
        self.color = "gray"

    def kolizja(self, other):
        if other.sila < 5 and other.__class__ != self.__class__:
            print("Zolw zablokowal atak", other.__class__.__name__)
        else:
            super().kolizja(other)