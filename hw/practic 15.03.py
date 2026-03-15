try:
    price = float(input("Введіть початкову ціну: "))
    discount = float(input("Введіть відсоток знижки: "))

    final_price = price - (price * discount / 100)

    print("Фінальна ціна:", final_price)

except ValueError:
    print("Помилка! Введіть число.")

try:
    dollars = float(input("Долари: "))
    rate = float(input("Курс: "))

    if rate == 0:
        raise Exception("Курс не може бути 0")

    euro = dollars / rate
    print("Євро:", euro)

except ValueError:
    print("Помилка введення")

except Exception as e:
    print(e)

finally:
    print("Операцію завершено")

try:
    marks = input("Оцінки: ")
    nums = [int(x) for x in marks.split()]

    avg = sum(nums) / len(nums)
    print("Середнє:", avg)

except ValueError:
    print("Вводьте тільки числа")

except ZeroDivisionError:
    print("Список порожній")

finally:
 print("Завершення обчислень")

 balance = 1000

try:
    money = int(input("Сума: "))

    if money % 10 != 0 or money > balance:
        raise Exception("Некоректна сума")

    print("Видача:", money)

except ValueError:
    print("Помилка введення")

except Exception as e:
    print(e)

finally:
    print("Транзакцію завершено")

try:
    order = input("Номер замовлення: ")

    if not order.startswith("ORD"):
        raise Exception("Неправильний формат")

    print("Номер правильний")

except Exception as e:
    print(e)

finally:
    print("Перевірку завершено")


try:
    text = input("Числа: ")
    numbers = []

    for i in text.split():
        try:
            numbers.append(float(i))
        except ValueError:
            print("Пропущено:", i)

    avg = sum(numbers) / len(numbers)
    print("Сума:", sum(numbers))
    print("Середнє:", avg)

except ZeroDivisionError:
    print("Немає чисел")

finally:
    print("Обробку завершено")





