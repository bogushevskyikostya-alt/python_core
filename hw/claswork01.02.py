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
        print(f"🎉 Вітаю! Ти вгадав число за {attempts} спроб.")
        break




    # Крок 1: Обрати фігуру
print("Оберіть фігуру:")
print("1 - Квадрат")
print("2 - Прямокутник")
choice = int(input("Введіть 1 або 2: "))

# Крок 2: Ввести розміри
if choice == 1:
    size = int(input("Введіть довжину сторони квадрата: "))
    width = height = size
elif choice == 2:
    width = int(input("Введіть ширину прямокутника: "))
    height = int(input("Введіть висоту прямокутника: "))
else:
    print("Невірний вибір!")
    exit()

# Крок 3: Символ заповнення
symbol = input("Введіть символ для заповнення фігури: ")

# Крок 4: Малюємо фігуру
for i in range(height):
    print(symbol * width)