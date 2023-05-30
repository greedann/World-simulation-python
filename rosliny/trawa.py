from roslina import Roslina

class Trawa(Roslina):
    def __init__(self, x, y, world):
        super().__init__(x, y, world)
        self.sila = 0
        self.color = "green"
