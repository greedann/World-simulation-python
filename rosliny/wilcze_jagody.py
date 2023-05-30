from roslina import Roslina

class WilczeJagody(Roslina):
    def __init__(self, x, y, world):
        super().__init__(x, y, world)
        self.sila = 99
        self.color = "blue"

    def kolizja(self, other):
        print("Wilcze jagody zabiły", other.__class__.__name__)
        super().kolizja(other)
        self.world.remove_organism(other)
