from zwierze import Zwierze

class Owca(Zwierze):
    def __init__(self, x, y, world):
        super().__init__(x, y, world)
        self.sila = 4
        self.inicjatywa = 4
        self.color = "white"