
class Organizm:
    def __init__(self, x, y, world):
        self.sila = 0
        self.inicjatywa = 0
        self.x = x
        self.y = y
        self.world = world
        self.age = 0
        self.color = None

    def akcja(self):
        pass

    def kolizja(self, organizm):
        pass

    def rysowanie(self):
        pass

    def __str__(self):
        return self.__class__.__name__ + ' ' + str(self.x) + ' ' + str(self.y) + ' ' + str(self.age)