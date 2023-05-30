from zwierze import Zwierze


class CyberOwca(Zwierze):
    def __init__(self, x, y, world):
        super().__init__(x, y, world)
        self.sila = 11
        self.inicjatywa = 4
        self.color = "black"

    def akcja(self):
        neardyest_barszcz = self.world.find_neardyest_barszcz(self.x, self.y)
        if neardyest_barszcz is not None:
            dx = neardyest_barszcz[0] - self.x
            dy = neardyest_barszcz[1] - self.y
            dx = dx // abs(dx) if dx != 0 else 0
            dy = dy // abs(dy) if dy != 0 else 0
            new_x = self.x + dx
            new_y = self.y + dy
            if self.world.is_ocuppied(new_x, new_y):
                print("CyberOwca kolizja", self.world.get_organism(
                    new_x, new_y).__class__.__name__)
                self.world.get_organism(new_x, new_y).kolizja(self)
            else:
                self.x = new_x
                self.y = new_y
        else:
            super().akcja()
