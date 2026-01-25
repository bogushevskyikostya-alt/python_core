a = int(input("Введи число: "))
n = int(input("Введи степінь (від 0 до 7): "))

if n < 0 or n > 7:
    print("Степінь введено неправильно")
else:
    result = 1
    i = 1
    while i <= n:
        result = result * a
        i = i + 1
    print("Результат:", result)

    n = int(input("Введи число від 1 до 100: "))

if n < 1 or n > 100:
    print("Помилка. Число не в діапазоні 1..100")
else:
    if n % 3 == 0 and n % 5 == 0:
        print("Fizz Buzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)

        # вибір закуски
print("Закуски:")
print("1 - Салат (5$)")
print("2 - Суп (7$)")
z = int(input("Обери закуску: "))

# вибір основної страви
print("Основні страви:")
print("1 - Курка (10$)")
print("2 - Риба (12$)")
m = int(input("Обери основну страву: "))

# вибір десерту
print("Десерти:")
print("1 - Морозиво (3$)")
print("2 - Фрукти (4$)")
d = int(input("Обери десерт: "))

client = int(input("Ти постійний клієнт? (1 - так, 0 - ні): "))

summa = 0

# ціни закусок
if z == 1:
    summa = summa + 5
    zakuska = "Салат"
else:
    summa = summa + 7
    zakuska = "Суп"

# ціни основних страв
if m == 1:
    summa = summa + 10
    main = "Курка"
else:
    summa = summa + 12
    main = "Риба"

# ціни десертів
if d == 1:
    summa = summa + 3
    desert = "Морозиво"
else:
    summa = summa + 4
    desert = "Фрукти"

discount = 0

# знижка за всі три страви
discount = discount + 10

# якщо сума більше 20
if summa > 20:
    discount = 15

# постійний клієнт
if client == 1:
    discount = discount + 5

# спеціальна пропозиція суп + риба
if zakuska == "Суп" and main == "Риба":
    summa = summa - 2

# курка + морозиво
if main == "Курка" and desert == "Морозиво":
    print("Вам додано безкоштовний напій: Чай")

# застосування знижки
summa = summa - (summa * discount / 100)

print("Сума до оплати:", summa, "$")
