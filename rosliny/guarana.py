from roslina import Roslina

class Guarana(Roslina):
    def __init__(self, x, y, world):
        super().__init__(x, y, world)
        self.sila = 0
        self.color = "pink"

    def kolizja(self, other):
        print("Guarana dodała 3 siły", other.__class__.__name__)
        other.sila += 3
        super().kolizja(other)