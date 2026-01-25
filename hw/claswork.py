a = int(input("Введи перше число: "))
b = int(input("Введи друге число: "))

a_temp = a
while a_temp <= b:
    print(a_temp)
    a_temp += 1

    a = int(input("Введи перше число: "))
b = int(input("Введи друге число: "))

a_temp = a
while a_temp <= b:
    if a_temp % 2 != 0:
        print(a_temp)
    a_temp += 1

    a = int(input("Введи перше число: "))
b = int(input("Введи друге число: "))

a_temp = b
while a_temp >= a:
    if a_temp % 2 == 0:
        print(a_temp)
    a_temp -= 1

    a = int(input("Введи перше число: "))
b = int(input("Введи друге число: "))
order = int(input("Введи 1 (зростання) або 2 (спадання): "))

if order == 1:
    a_temp = a
    while a_temp <= b:
        print(a_temp)
        a_temp += 1
else:
    a_temp = b
    while a_temp >= a:
        print(a_temp)
        a_temp -= 1

        a = int(input("Введи перше число: "))
b = int(input("Введи друге число: "))

if a > b:
    a = a + b
    b = a - b
    a = a - b

a_temp = a
while a_temp <= b:
    if a_temp % 2 != 0:
        print(a_temp)
    a_temp += 1

    a = int(input("Введи перше число: "))
b = int(input("Введи друге число: "))

# нормалізація меж
if a > b:
    a = a + b
    b = a - b
    a = a - b

# парні числа у зростаючому порядку
a_temp = a
while a_temp <= b:
    if a_temp % 2 == 0:
        print(a_temp)
    a_temp += 1

# непарні числа у спадному порядку
a_temp = b
while a_temp >= a:
    if a_temp % 2 != 0:
        print(a_temp)
    a_temp -= 1
    
