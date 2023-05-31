
from random import randint, random, choice
from organizm import Organizm
from czlowiek import Czlowiek
from roslina import Roslina
from zwierzes.antylopa import Antylopa
from zwierzes.wilk import Wilk
from zwierzes.zolw import Zolw
from zwierzes.owca import Owca
from zwierzes.lis import Lis
from zwierzes.cyber_owca import CyberOwca

from rosliny.guarana import Guarana
from rosliny.barscz_sosnowskiego import BarsczSosnowskiego
from rosliny.trawa import Trawa
from rosliny.mlecz import Mlecz
from rosliny.wilcze_jagody import WilczeJagody


class World:
    def __init__(self, width, height):
        self.organisms = []
        self.width = width
        self.height = height
        self.turn = 0
        self.human = None
        for _ in range(int(width * height / 15)):
            self.add_random_organism()

    def add_organism(self, organism, x, y):
        if self.is_ocuppied(x, y):
            return
        if organism == "Czlowiek":
            self.human = Czlowiek(x, y, self)
            self.organisms.append(self.human)
        elif organism == "Wilk":
            self.organisms.append(Wilk(x, y, self))
        elif organism == "Owca":
            self.organisms.append(Owca(x, y, self))
        elif organism == "Lis":
            self.organisms.append(Lis(x, y, self))
        elif organism == "Zolw":
            self.organisms.append(Zolw(x, y, self))
        elif organism == "Antylopa":
            self.organisms.append(Antylopa(x, y, self))
        elif organism == "CyberOwca":
            self.organisms.append(CyberOwca(x, y, self))
        elif organism == "Guarana":
            self.organisms.append(Guarana(x, y, self))
        elif organism == "BarsczSosnowskiego":
            self.organisms.append(BarsczSosnowskiego(x, y, self))
        elif organism == "Trawa":
            self.organisms.append(Trawa(x, y, self))
        elif organism == "Mlecz":
            self.organisms.append(Mlecz(x, y, self))
        elif organism == "WilczeJagody":
            self.organisms.append(WilczeJagody(x, y, self))

    def add_random_organism(self):
        organisms = [Antylopa, Wilk, Zolw, Owca, Lis, CyberOwca,
                     Guarana, BarsczSosnowskiego, Trawa, Mlecz, WilczeJagody]
        x = randint(0, self.width - 1)
        y = randint(0, self.height - 1)
        organism = choice(organisms)(x, y, self)
        self.organisms.append(organism)

    def remove_organism(self, organism) -> None:
        if organism in self.organisms:
            self.organisms.remove(organism)
        elif organism == self.human:
            self.human.color = None

    def get_organism(self, x, y):
        for organism in self.organisms:
            if organism.x == x and organism.y == y:
                return organism
        return None

    def next_turn(self):
        self.turn += 1
        self.organisms.sort(
            key=lambda organism: organism.inicjatywa, reverse=True)
        for organism in self.organisms:
            organism.akcja()

    def kill_zwierze_neardy(self, x, y):
        for organism in self.organisms:
            if abs(organism.x-x) <= 1 and abs(organism.y-y) <= 1:
                if organism.initiative != 0:
                    self.remove_organism(organism)

    def is_ocuppied(self, x, y):
        return self.get_organism(x, y) is not None

    def find_free_neardy(self, x, y) -> list[2]:
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if not self.is_ocuppied(x + dx, y + dy):
                    return [x + dx, y + dy]
        return None

    def save_to_file(self, file_name):
        with open('./saves/'+file_name, 'w') as file:
            file.write(str(self.turn) + '\n')
            file.write(str(self.width) + '\n')
            file.write(str(self.height) + '\n')
            file.write(str(self.human)+' ' +
                       str(self.human.umiejetnosc) + '\n')
            file.write(str(len(self.organisms)) + '\n')
            for organism in self.organisms:
                file.write(str(organism) + '\n')

    def load_from_file(self, file_name):
        with open('./saves/'+file_name, 'r') as file:
            self.turn = int(file.readline())
            self.width = int(file.readline())
            self.height = int(file.readline())
            self.human = Czlowiek(0, 0, self)
            parameters = file.readline().split()
            parameters = [int(x) for x in parameters[1:]]
            self.human.x, self.human.y, self.human.age, self.human.umiejetnosc = parameters
            self.organisms = []
            for _ in range(int(file.readline())):
                parameters = file.readline().split()
                cls = globals()[parameters[0]]
                parameters = [int(x) for x in parameters[1:]]
                organism = cls(parameters[0], parameters[1], self)
                organism.wiek = parameters[2]
                self.organisms.append(organism)

    def find_neardyest_barszcz(self, x, y):
        barszcz_pos = None
        min_distance = 100000
        for organism in self.organisms:
            if organism.__class__.__name__ == "BarsczSosnowskiego":
                distance = abs(organism.x-x) + abs(organism.y-y)
                if distance < min_distance:
                    min_distance = distance
                    barszcz_pos = [organism.x, organism.y]
        return barszcz_pos
