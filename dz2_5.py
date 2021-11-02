price_list = [120.8, 45.8, 100, 65.8, 71.2, 25, 33.85, 75.33, 68, 76.55]

print(id(price_list), price_list)
price_list.sort()
print(id(price_list), price_list)
price_list_reverse = sorted(price_list, reverse=True)
print(id(price_list_reverse), price_list_reverse)
print(price_list[5:])

i = 0
while i < len(price_list):
    price_list[i] = str(float(price_list[i]))
    price_list[i] = price_list[i].split('.')
    price_list[i] = str(f'{price_list[i][0]} руб {price_list [i][1]} коп')
    i = i+1

price_list = ', '.join(price_list)
print(price_list)

