number = int(input("Введіть число: "))

for i in range(1, 11):
    print(f"{number} * {i} = {number * i}")



    for n in range(1, 10):
     print(f"{n} * {i} = {n * i}")


     n = int(input("Скільки чисел ви хочете ввести? "))

max_number = None

for i in range(n):
    num = int(input(f"Введіть число {i+1}: "))
    if max_number is None or num > max_number:
        max_number = num

print("Найбільше число:", max_number)



import random

secret = random.randint(1, 500)
attempts = 0

print("Я загадав число від 1 до 500. Спробуй вгадати!")
print("Введи 0, якщо хочеш вийти з гри.")

while True:
    guess = int(input("Твоя спроба: "))

    if guess == 0:
        print("Гру завершено. Загадане число було:", secret)
        break

    attempts += 1

    if guess < secret:
        print("Більше!")
    elif guess > secret:
        print("Менше!")
    else:
        print(f" Вітаю! Ти вгадав число за {attempts} спроб.")
        break




    
print("Оберіть фігуру:")
print("1 - Квадрат")
print("2 - Прямокутник")
choice = int(input("Введіть 1 або 2: "))


if choice == 1:
    size = int(input("Введіть довжину сторони квадрата: "))
    width = height = size
elif choice == 2:
    width = int(input("Введіть ширину прямокутника: "))
    height = int(input("Введіть висоту прямокутника: "))
else:
    print("Невірний вибір!")
    exit()


symbol = input("Введіть символ для заповнення фігури: ")


for i in range(height):
    print(symbol * width)

    # Введення розмірів
width = int(input("Введіть ширину прямокутника: "))
height = int(input("Введіть висоту прямокутника: "))

# Малюємо прямокутник
for i in range(height):
    print("*" * width)
    


    print("Оберіть фігуру:")
print("1 - Квадрат")
print("2 - Прямокутник")
choice = int(input("Введіть 1 або 2: "))

if choice == 1:
    size = int(input("Введіть довжину сторони квадрата: "))
    width = height = size
elif choice == 2:
    width = int(input("Введіть ширину прямокутника: "))
    height = int(input("Введіть висоту прямокутника: "))
else:
    print("Невірний вибір!")
    exit()

symbol = input("Введіть символ для заповнення фігури: ")

for i in range(height):
    print(symbol * width)


    size = int(input("Введіть розмір сторони квадрата: "))

for i in range(size):
    if i == 0 or i == size - 1:
        print("*" * size)  # Верх і низ
    else:
        print("*" + " " * (size - 2) + "*")  # Середина



        width = int(input("Введіть ширину прямокутника: "))
height = int(input("Введіть висоту прямокутника: "))

for i in range(height):
    if i == 0 or i == height - 1:
        print("*" * width)
    else:
        print("*" + " " * (width - 2) + "*")


        height = int(input("Введіть висоту трикутника: "))
symbol = input("Введіть символ: ")

for i in range(1, height + 1):
    print(symbol * i)


    height = int(input("Введіть висоту трикутника: "))
symbol = input("Введіть символ: ")

for i in range(1, height + 1):
    print(" " * (height - i) + symbol * (2 * i - 1))

    