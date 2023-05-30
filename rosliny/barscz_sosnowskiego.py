from roslina import Roslina
from zwierze import Zwierze

class BarsczSosnowskiego(Roslina):
    def __init__(self, x, y, world):
        super().__init__(x, y, world)
        self.sila = 10
        self.color = "magenta"

    def akcja(self):
        for organizm in self.world.organisms:
            if (abs(organizm.x -self.x)<=1 and abs(organizm.y -self.y)<=1 and issubclass(organizm.__class__, Zwierze)):
                if (organizm.__class__.__name__ == "CyberOwca"):
                    continue
                print("Barszcz zabil", organizm.__class__.__name__)
                self.world.remove_organism(organizm)
        super().akcja()

    def kolizja(self, other):
        print("Barszcz kolizja z", other.__class__.__name__)
        if (other.__class__.__name__ != "CyberOwca"):
            print("Barszcz zabil", other.__class__.__name__)
            self.world.remove_organism(other)
        else:
            print("Barszcz zostal zjedzony przez", other.__class__.__name__)
            self.world.remove_organism(self)

