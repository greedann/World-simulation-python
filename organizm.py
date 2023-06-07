
class Organizm:
    def __init__(self, x, y, world):
        self.__sila = 0
        self.__inicjatywa = 0
        self.__x = x
        self.__y = y
        self.__world = world
        self.__age = 0
        self.__color = None

    @property
    def sila(self):
        return self.__sila
    
    @sila.setter
    def sila(self, value):
        self.__sila = value
    
    @property
    def inicjatywa(self):
        return self.__inicjatywa
    
    @inicjatywa.setter
    def inicjatywa(self, value):
        self.__inicjatywa = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if (value >= 0 and value < self.__world.width):
            self.__x = value

    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, value):
        if (value >= 0 and value < self.__world.height):
            self.__y = value
        
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):
        self.__age = value

    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, value):
        self.__color = value

    @property
    def world(self):
        return self.__world


    def akcja(self):
        pass

    def kolizja(self, organizm):
        pass

    def rysowanie(self):
        pass

    def __str__(self):
        return self.__class__.__name__ + ' ' + str(self.x) + ' ' + str(self.y) + ' ' + str(self.age)