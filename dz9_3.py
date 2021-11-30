class Worker:
    def __init__(self, name, surname, income, position):
        self.name = name
        self.surname = surname
        self._income = income
        self.position = position


class Position(Worker):
    def get_fullname(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


income_direct = {'wage': 10, 'bonus': 5}
pos = Position('Liu', 'Kang', income_direct, 'Grand_Master')
print(pos.get_total_income())
print(pos.get_fullname())
