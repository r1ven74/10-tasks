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

















