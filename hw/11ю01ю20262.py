seconds_passed = int(input("Введіть кількість секунд від початку дня: "))

choice = input("Що порахувати? (h - години, m - хвилини, s - секунди): ")

seconds_in_day = 24 * 60 * 60
remaining = seconds_in_day - seconds_passed

if choice == "h":
    print("Залишилось годин:", remaining // 3600)
elif choice == "m":
    print("Залишилось хвилин:", remaining // 60)
elif choice == "s":
    print("Залишилось секунд:", remaining)
else:
    print("Невірний вибір")

    import math

diameter = float(input("Введіть діаметр кола: "))
choice = input("Що порахувати? (s - площа, p - периметр): ")

radius = diameter / 2

if choice == "s":
    print("Площа кола:", math.pi * radius ** 2)
elif choice == "p":
    print("Периметр кола:", math.pi * diameter)
else:
    print("Невірний вибір")

    #price = float(input("вартість однієї приставки: "))
    count= int(input("кількість приставок: "))
    discount = int(input("знижка в %: "))

    choice = input("Що порахувати? (t - загальна сума, o - ціна однієї зі знижкою): ")

discount_price = price - price * discount / 100

if choice == "t":
    print("Загальна сума:", discount_price * count)
elif choice == "o":
    print("Ціна однієї зі знижкою:", discount_price)
else:
    print("Невірний вибір")

    file_size_gb = float(input("Введіть розмір файлу (ГБ): "))
speed_bps = float(input("Введіть швидкість (біт/с): "))

choice = input("У чому показати час? (h - години, m - хвилини, s - секунди): ")

file_size_bits = file_size_gb * 8 * 1024 * 1024 * 1024
time_seconds = file_size_bits / speed_bps

if choice == "h":
    print("Час завантаження (години):", time_seconds / 3600)
elif choice == "m":
    print("Час завантаження (хвилини):", time_seconds / 60)
elif choice == "s":
    print("Час завантаження (секунди):", time_seconds)
else:
    print("Невірний вибір")

    hour = int(input("Введіть кількість годин (0–23): "))

if 0 <= hour < 6:
    print("Good Night")
elif 6 <= hour < 13:
    print("Good Morning")
elif 13 <= hour < 17:
    print("Good Day")
elif 17 <= hour < 24:
    print("Good Evening")
else:
    print("Невірне значення")

    temp = float(input("Введіть температуру (°C): "))

if temp < -10:
    print("Дуже холодно")
elif -10 <= temp < 0:
    print("Холодно")
elif 0 <= temp < 15:
    print("Прохолодно")
elif 15 <= temp <= 25:
    print("Тепло")
else:
    print("Спекотно")
    

