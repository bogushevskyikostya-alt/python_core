s = input("Введіть рядок: ")

letters = 0
digits = 0

for ch in s:
    if ch.isalpha():
        letters += 1
    elif ch.isdigit():
        digits += 1

print("Кількість букв:", letters)
print("Кількість цифр:", digits)

s = input("Введіть рядок: ")
symbol = input("Введіть символ для пошуку: ")

count = 0
for ch in s:
    if ch == symbol:
        count += 1

print("Кількість входжень:", count)

s = input("Введіть рядок: ")

reversed_s = ""
for ch in s:
    reversed_s = ch + reversed_s

print("Результат:", reversed_s)

s = input("Введіть рядок: ")
word = input("Введіть слово для пошуку: ")

words = s.split()
count = 0

for w in words:
    if w == word:
        count += 1

print("Кількість входжень:", count)

s = input("Введіть рядок: ")
old_word = input("Слово для пошуку: ")
new_word = input("Слово для заміни: ")

result = s.replace(old_word, new_word)

print("Результат:", result)

s = input("Введіть рядок: ")

words = s.split()
longest = ""

for w in words:
    if len(w) > len(longest):
        longest = w

print("Найдовше слово:", longest)