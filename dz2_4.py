posts_and_names = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
                   'директор алита']

for i in posts_and_names:
    print('Привет, 'f'{i.split()[-1].title()}')
