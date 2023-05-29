from organizm import Organizm


class Czlowiek(Organizm):
    def __init__(self, x, y, world):
        super().__init__(x, y, world)
        self.sila = 5
        self.inicjatywa = 4
        self.umiejetnosc = 0
        self.color = 'red'

    def akcja(self, dx, dy):
        self.age += 1

        new_x = self.x + dx
        new_y = self.y + dy

        if (new_x >= 0 and new_x < self.world.width and new_y >= 0 and new_y < self.world.height):
            self.x += dx
            self.y += dy

        if (self.umiejetnosc > 0):
            self.umiejetnosc -= 1
            if (self.umiejetnosc == 0):
                self.umiejetnosc = -5
        elif (self.umiejetnosc < 0):
            self.umiejetnosc += 1