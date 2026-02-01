height = int(input("Введіть висоту трикутника: "))
symbol = input("Введіть символ: ")

for i in range(1, height + 1):
    print(" " * (height - i) + symbol * (2 * i - 1))