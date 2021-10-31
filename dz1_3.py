a = int(input("Введите число от 1 до 100: "))
if a == 1 or a == 21 or a == 31 or a == 41 or a == 51 or a == 61 or a == 71 or a == 81 or a == 91:
    print(a, "процент")
elif a > 1 and a < 5 or a > 21 and a < 25 or a > 31 and a < 35 or a > 41 and a < 45 \
        or a > 51 and a < 55 or a > 61 and a < 65 or a > 71 and a < 75 or a > 81 and a < 85 or a > 91 and a < 95:
    print(a, "процента")
else:
    print(a, "процентов")
