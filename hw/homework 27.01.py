a = int(input("Введи початок: "))
b = int(input("Введи кінець: "))

if a > b:
    a = a + b
    b = a - b
    a = a - b

a_temp = a
while a_temp <= b:
    if a_temp % 7 == 0:
        print(a_temp)
    a_temp = a_temp + 1

    a = int(input("Введи початок: "))
b = int(input("Введи кінець: "))

if a > b:
    a = a + b
    b = a - b
    a = a - b

# всі числа
a_temp = a
while a_temp <= b:
    print(a_temp)
    a_temp = a_temp + 1

# у спадному порядку
a_temp = b
while a_temp >= a:
    print(a_temp)
    a_temp = a_temp - 1

# числа кратні 7
a_temp = a
while a_temp <= b:
    if a_temp % 7 == 0:
        print(a_temp)
    a_temp = a_temp + 1

# кількість чисел кратних 5
count = 0
a_temp = a
while a_temp <= b:
    if a_temp % 5 == 0:
        count = count + 1
    a_temp = a_temp + 1

print("Кількість чисел, кратних 5:", count)

a = int(input("Введи початок: "))
b = int(input("Введи кінець: "))

if a > b:
    a = a + b
    b = a - b
    a = a - b

a_temp = a
while a_temp <= b:
    if a_temp % 3 == 0 and a_temp % 5 == 0:
        print("Fizz Buzz")
    elif a_temp % 3 == 0:
        print("Fizz")
    elif a_temp % 5 == 0:
        print("Buzz")
    else:
        print(a_temp)
    a_temp = a_temp + 1

    a = int(input("Введи початок: "))
b = int(input("Введи кінець: "))
step = int(input("Введи крок: "))
order = int(input("1 - прямо, 2 - назад: "))

if order == 1:
    a_temp = a
    while a_temp <= b:
        print(a_temp)
        a_temp = a_temp + step
else:
    a_temp = b
    while a_temp >= a:
        print(a_temp)
        a_temp = a_temp - step

        a = int(input("Введи початок: "))
b = int(input("Введи кінець: "))

if a > b:
    a = a + b
    b = a - b
    a = a - b

result = 1
found = 0

a_temp = a
while a_temp <= b:
    if a_temp % 4 == 0 and a_temp % 6 != 0:
        result = result * a_temp
        found = 1
    a_temp = a_temp + 1

if found == 1:
    print("Добуток:", result)
else:
    print("Таких чисел немає")

    a = int(input("Введи число A: "))
n = int(input("Введи степінь N: "))

result = 1
count = 1

while count <= n:
    result = result * a
    count = count + 1

print("Результат:", result)
