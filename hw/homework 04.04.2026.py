import random
import string

# Ввід базового імені
name = input("Введіть базове ім'я: ")

# 🔹 Варіант 1 (Цифровий)
nick1 = name + str(random.randint(100, 9999))

# 🔹 Варіант 2 (Літерний)
symbols = ['_', '.', '-']
symbol = random.choice(symbols)
letters = ''.join(random.choices(string.ascii_lowercase, k=3))
nick2 = name + symbol + letters

# 🔹 Варіант 3 (Елітний)
prefixes = ['Pro', 'Super', 'Ultra']
prefix = random.choice(prefixes)

name_cap = name.capitalize()
digits = ''.join(random.choices(string.digits, k=2))

# перемішуємо ім'я + цифри
mix = list(name_cap + digits)
random.shuffle(mix)
mixed_name = ''.join(mix)

nick3 = prefix + mixed_name

# 🔥 Вивід
print("\n🔥 Ваші унікальні нікнейми:")
print(f"1️⃣ Цифровий: {nick1}")
print(f"2️⃣ Літерний: {nick2}")
print(f"3️⃣ Елітний: {nick3}")

def draw_header(title):
    width = 40
    print("=" * width)
    print(title.center(width))
    print("=" * width)


def draw_menu(options_list):
    for i, option in enumerate(options_list, start=1):
        print(f"[ {i} ] {option}")


def draw_warning(message):
    border = "!" * (len(message) + 4)
    print(border)
    print(f"! {message} !")
    print(border)

    import console_ui

# Заголовок
console_ui.draw_header("🎮 Ласкаво просимо в гру!")

# Меню
options = ["Почати гру", "Налаштування", "Вийти"]
console_ui.draw_menu(options)

# Ввід користувача
choice = input("\nОберіть пункт меню: ")

# Перевірка
if choice not in ['1', '2', '3']:
    console_ui.draw_warning("Невірний вибір!")
else:
    print(f"\nВи обрали пункт: {choice}")
    