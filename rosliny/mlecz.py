from roslina import Roslina


class Mlecz(Roslina):
    def __init__(self, x, y, world):
        super().__init__(x, y, world)
        self.sila = 0
        self.color = "yellow"

    def akcja(self):
        for _ in range(3):
            super().akcja()
