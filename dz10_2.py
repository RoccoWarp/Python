from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def calc_fabric(self):
        pass


class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def calc_fabric(self):
        return self.v / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def calc_fabric(self):
        return self.h * 2 + 0.3


c = Coat(40)
print(c.calc_fabric)
s = Suit(190)
print(s.calc_fabric)
