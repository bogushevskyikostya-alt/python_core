import random


nums = list(map(int, input("Завдання 1\nВведіть числа через пробіл: ").split()))
unique_nums = set(nums)
print("Унікальні елементи:", unique_nums)

print("\n-------------------")


set1 = set(random.randint(1, 20) for _ in range(10))
set2 = set(random.randint(1, 20) for _ in range(10))

print("Завдання 2")
print("Множина 1:", set1)
print("Множина 2:", set2)

print("Спільні елементи:", set1 & set2)
print("Різниця (set1 - set2):", set1 - set2)
print("Об’єднання:", set1 | set2)

print("\n-------------------")

print("Завдання 3")
word1 = input("Введіть перше слово: ").lower()
word2 = input("Введіть друге слово: ").lower()

if set(word1) == set(word2):
    print("Слова є анаграмами")
else:
    print("Слова НЕ є анаграмами")

    