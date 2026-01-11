# number = int(input(`число: `))
#if number %2 ==0
#     print(`even number`)
#else:
#     print(`odd number`)

# number = int(input(`число: `))
#if number %7 ==0
#     print(`Number is multiple 7`)
# else:
#     print(`Number is not multiple 7`)

# number 1 = int(input(`2 числа: `))
# number 2 = int(input(`число': `))
# if number1 > number2:
print("First number is greater")
#else:
#     print("Second number is greater")

#number1= int(input("число: "))
#number2= int(input("число: "))

#if number1 < number2:
#    print("First number is smaller")
#else:
#    print("Second number is smaller")

a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))

print("Оберіть операцію:")
print("1 - сума")
print("2 - різниця")
print("3 - добуток")
print("4 - середнє арифметичне")

choice = input("Ваш вибір: ")

if choice == "1":
    print("Сума =", a + b)
elif choice == "2":
    print("Різниця =", a - b)
elif choice == "3":
    print("Добуток =", a * b)
elif choice == "4":
    print("Середнє арифметичне =", (a + b) / 2)
else:
    print("Невірний вибір")

    usd = float(input("Введіть суму в доларах: "))

print("Оберіть валюту:")
print("EUR - євро")
print("GBP - фунти")
print("UAH - гривні")

currency = input("Введіть валюту: ")

rate = float(input("Введіть курс до долара: "))

if currency == "EUR":
    print("Сума в євро:", usd * rate)
elif currency == "GBP":
    print("Сума у фунтах:", usd * rate)
elif currency == "UAH":
    print("Сума у гривнях:", usd * rate)
else:
    print("Невірна валюта")
