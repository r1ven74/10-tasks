#1
try:
    num = int(input("Введите число"))
    if num > 0:
        print("Число положительное")
except ValueError:
    print("Пиши число")

#2
try:
    num = int(input("Введите число"))
    if num % 2 == 0:
        print("Число четное")
    else:
        print("Число нечетное")
except ValueError:
    print("Введи число")

#3
try:
    num = int(input("Введите число"))
    if num > 9 and num < 21:
        print("true")
    else:
        print("false")
except ValueError:
    print("Пиши число")

#4
try:
    num = int(input("Введите число"))
    num_2 = int(input("Введите число"))
    if num > 9 and num_2 > 9:
        print("true")
    else:
        print("false")
except ValueError:
    print("Пиши число")

#5
try:
    num = int(input("Введите число"))
    if num == 0:
        print("0")
    else:
        if num > 0:
            print("положительное")
        else:
            if num < 0:
                print("отрицательное")
except ValueError:
    print("Введите число")

#6
try:
    num = int(input("Введите число"))
    num_2 = int(input("Введите число"))
    num_3 = int(input("Введите число"))
    if num % 2 == 0 or num_2 % 2 == 0 or num_3 % 2 == 0:
        print("Есть четное число")
except ValueError:
    print("введи число")

#7
try:
    num = int(input('Введите число'))
    if num < 10:
        print('Меньше 10')
    elif num > 9 < 21:
        print('Между 10 и 20')
    elif num > 20:
        print("Больше 20")
except(ValueError):
    print('введи число')
#8
password = input('Введите пароль')
if password == 'password2323':
    print("Доступ разрешен")
else:
    print("Доступ запрещен")
#9
try:
    num = int(input('Введите число'))
    if num % 400 == 0 or num % 4 == 0 and num % 100 != 0:
        print('Високосный')
    else:
        print('Не високосный')
except(ValueError):
    print('Введите число')
#10
try:
    num = int(input('Введите число'))
    num_2 = int(input('Введите число'))
    num_3 = int(input('Введите число'))
    if num > num_2:
        if num > num_3:
            print(num)
        else:
            print(num_3)
    elif num_2 > num_3:
        print(num_2)
    else:
        print(num_3)
except(ValueError):
    print('Введите число')

















