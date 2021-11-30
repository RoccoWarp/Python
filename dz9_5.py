class Stationary:
    def __init__(self, title):
        self.title = title

    @staticmethod
    def drow():
        print('Запуск отрисовки')


class Pen(Stationary):
    @staticmethod
    def drow():
        print('Pen')


class Pencil(Stationary):
    @staticmethod
    def drow():
        print('Pencil')


class Handle(Stationary):
    @staticmethod
    def drow():
        print('Handle')
