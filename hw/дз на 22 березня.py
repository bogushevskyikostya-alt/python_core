try:
    a = float(input("Перше число: "))
    b = float(input("Друге число: "))

    result = a / b
    print("Результат:", result)

except ValueError:
    print("Помилка! Введіть числа.")

except ZeroDivisionError:
    print("Ділити на нуль не можна.")

finally:
    print("Операцію завершено")

    numbers = [10, 20, 30, 40, 50]

try:
    index = int(input("Введіть індекс: "))
    print("Елемент:", numbers[index])

except ValueError:
    print("Індекс має бути числом")

except IndexError:
    print("Індекс поза межами списку")

finally:
    print("Операцію завершено")

    try:
    sales = input("Введіть продажі: ")
    nums = []

    for i in sales.split():
        nums.append(float(i))

    total = sum(nums)
    print("Загальна сума:", total)

    except ValueError:
    print("Помилка введення")

    finally:
    print("Обробку завершено")

import math

try:
    num = float(input("Введіть число: "))

    if num < 0:
        raise Exception("Не можна обчислити корінь від від'ємного числа")

    print("Корінь:", math.sqrt(num))

except ValueError:
    print("Введіть число")

except Exception as e:
    print(e)

finally:
    print("Обчислення завершено")


    try:
    text = input("Введіть товар (назва, ціна, кількість): ")

    parts = text.split(",")

    name = parts[0]
    price = float(parts[1])
    amount = int(parts[2])

    print("Товар:", name)
    print("Ціна:", price)
    print("Кількість:", amount)

    except ValueError:
    print("Помилка в числах")

    finally:
    print("Парсинг завершено")

    import random

def connect_to_server():
    if random.randint(0, 1) == 0:
        raise ConnectionError("Помилка підключення")
    else:
        return "Підключення успішне"

try:
    print(connect_to_server())

except ConnectionError:
    print("Не вдалося підключитися до сервера")

finally:
    print("Спробу завершено")
    


