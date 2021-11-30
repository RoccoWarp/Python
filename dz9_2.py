class Road:
    THICKNESS = 5
    WEIGHT = 25

    def __init__(self, lengh, width):
        self._length = lengh
        self._width = width

    def calc_mass(self):
        return(self._length * self._width * self.WEIGHT * self.THICKNESS)


road_2 = Road(5000, 20)
print(road_2.calc_mass()/1000)
