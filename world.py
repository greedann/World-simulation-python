
from random import randint, random, choice
from organizm import Organizm
from czlowiek import Czlowiek
from roslina import Roslina
from zwierze import Zwierze


class World:
    moves = ['up', 'down', 'left', 'right', 'stop']

    def __init__(self, width, height):
        self.organisms = []
        self.width = width
        self.height = height
        self.turn = 0
        for _ in range(int(width * height / 15)):
            self.add_random_organism()

    def add_organism(self, organism, x, y):
        if self.is_ocuppied(x, y):
            return
        if organism == "Czlowiek":
            self.human = Czlowiek(x, y, self)
            self.organisms.append(self.human)
        elif organism == "Roslina":
            self.organisms.append(Roslina(x, y, self))

    def add_random_organism(self):
        organisms = [Roslina, Zwierze]
        x = randint(0, self.width - 1)
        y = randint(0, self.height - 1)
        organism = choice(organisms)(x, y, self)
        self.organisms.append(organism)

    def remove_organism(self, organism) -> None:
        self.organisms.remove(organism)

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
        with open(file_name, 'w') as file:
            file.write(str(self.turn) + '\n')
            file.write(str(self.width) + '\n')
            file.write(str(self.height) + '\n')
            file.write(str(self.human) + '\n')
            file.write(str(len(self.organisms)) + '\n')
            for organism in self.organisms:
                file.write(str(organism) + '\n')

    def load_from_file(self, file_name):
        with open(file_name, 'r') as file:
            self.turn = int(file.readline())
            self.width = int(file.readline())
            self.height = int(file.readline())
            self.human = Czlowiek(self, 0, 0)
            self.human.load_from_file(file)
            self.organisms = []
            for _ in range(int(file.readline())):
                organism = Organizm(self, 0, 0)
                organism.load_from_file(file)
                self.organisms.append(organism)
