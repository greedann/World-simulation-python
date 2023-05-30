from zwierze import Zwierze

class Wilk(Zwierze):
    def __init__(self, x, y, world):
        super().__init__(x, y, world)
        self.sila = 9
        self.inicjatywa = 5
        self.color = "darkgray"