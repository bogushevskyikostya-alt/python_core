a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
c = float(input("Введіть третє число: "))

choice = input("Виберіть операцію (сума / добуток): ")

if choice == "сума":
    print("Сума:", a + b + c)
elif choice == "добуток":
    print("Добуток:", a * b * c)
else:
    print("Помилка вибору")

    a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
c = float(input("Введіть третє число: "))

choice = input("Вибір (max / min / avg): ")

if choice == "max":
    print("Максимум:", max(a, b, c))
elif choice == "min":
    print("Мінімум:", min(a, b, c))
elif choice == "avg":
    print("Середнє арифметичне:", (a + b + c) / 3)
else:
    print("Помилка вибору")

    grade = int(input("Введіть оцінку (1-5): "))

if grade == 1:
    print("Дуже погано")
elif grade == 2:
    print("Погано")
elif grade == 3:
    print("Задовільно")
elif grade == 4:
    print("Добре")
elif grade == 5:
    print("Відмінно")
else:
    print("Помилка: оцінка має бути від 1 до 5")

    meters = float(input("Введіть кількість метрів: "))

print("1 — Мілі")
print("2 — Дюйми")
print("3 — Ярди")
print("4 — Усі три")
print("5 — Кілометри і сантиметри")

choice = int(input("Ваш вибір: "))

if choice == 1:
    print("Мілі:", meters / 1609.34)
elif choice == 2:
    print("Дюйми:", meters * 39.37)
elif choice == 3:
    print("Ярди:", meters * 1.094)
elif choice == 4:
    print("Мілі:", meters / 1609.34)
    print("Дюйми:", meters * 39.37)
    print("Ярди:", meters * 1.094)
elif choice == 5:
    print("Кілометри:", meters / 1000)
    print("Сантиметри:", meters * 100)
else:
    print("Помилка вибору")

    a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))

op = input("Операція (+ - * / % **): ")

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    if b != 0:
        print(a / b)
    else:
        print("Ділення на нуль")
elif op == "%":
    print(a % b)
elif op == "**":
    print(a ** b)
else:
    print("Невідома операція")

    num = input("Введіть тризначне число: ")

if len(num) != 3 or not num.isdigit():
    print("Помилка")
else:
    if num[0] == num[1] == num[2]:
        print("Всі цифри однакові")
    else:
        print("Цифри різні")
        