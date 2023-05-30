from zwierze import Zwierze

class Lis(Zwierze):
    def __init__(self, x, y, world):
        super().__init__(x, y, world)
        self.sila = 3
        self.inicjatywa = 7
        self.color = "orange"
        self.wech = True