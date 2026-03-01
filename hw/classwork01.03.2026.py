def print_quote():
    text = """
    "Don't let the noise of others' opinions
          drown out your own inner voice."
                    Steve Jobs
    """
    print(text)

# Виклик:
print_quote()

def print_odd_numbers(start, end):
    # Використовуємо min/max на випадок, якщо числа передані не по порядку
    for i in range(min(start, end), max(start, end) + 1):
        if i % 2 != 0:
            print(i, end=" ")
    print() # Новий рядок

# Приклад:
print_odd_numbers(1, 10) # Виведе: 1 3 5 7 9

def draw_line(length, direction, symbol):
    if direction.lower() == "горизонтальна":
        print(symbol * length)
    elif direction.lower() == "вертикальна":
        for _ in range(length):
            print(symbol)
    else:
        print("Помилка: напрямок має бути 'горизонтальна' або 'вертикальна'")

# Приклад:
draw_line(5, "горизонтальна", "*")

def get_max_of_four(a, b, c, d):
    return max(a, b, c, d)

# Приклад:
print(get_max_of_four(10, 55, 2, 18)) # Виведе: 55

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# Приклад:
print(is_prime(7))  # True
print(is_prime(10)) # False

def is_lucky_number(number):
    s = str(number)
    if len(s) != 6:
        return False # Перевірка, що число саме шестизначне
    
    # Перетворюємо символи на числа і рахуємо суми
    sum1 = int(s[0]) + int(s[1]) + int(s[2])
    sum2 = int(s[3]) + int(s[4]) + int(s[5])
    
    return sum1 == sum2

# Приклад:
print(is_lucky_number(123420)) # True
print(is_lucky_number(723422)) # False
