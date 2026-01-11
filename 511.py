print("hello!")
print(type(10 / 5))
#Змінна- іменована область памяті що зберігаєзначення певного типу і може йогозмінювати
group = "П511"
print(type(group))
group = 511
print(type(group))
print(10,12,14)
print(10)
print(10,5,6,6 ,sep='-')
print("Hello world")
weather = input("Введіть поточну погоду")
print(weather)
number1=input("Введіть перше число")
print{}
number2=input("Введіть друге число")
print(f{number1} **{number2}={number1 ** number2})
# bool- True або False
can_pinguins_swim = True
can_pinguins_fly = False
can_pinguins_swim = True
can_pinguins_fly = False

print(f'Чи можуть пінгвіни плавати? {can_pinguins_swim}')
print(f'Чи можуть пінгвіни літати? {can_pinguins_fly}')
print(type(can_pinguins_fly))
print(type(can_pinguins_swim))
 number = int(input("Введіть ціле число: "))

print(f'{number} > 10? {number > 10}')
print(f'{number} >= 10? {number >= 10}')
print(f'{number} < 10? {number < 10}')
print(f'{number} <= 10? {number <= 10}')
print(f'{number} == 10? {number == 10}')
print(f'{number} != 10? {number != 10}')
is cold = input("Чи зараз холодно на вулиці (так/ні)? ")
if is cold == "так":
    print("Вдягаємо теплий одяг")

else:
    print("Вдягаймо легкий одяг")

print("Виходимо на вулицю")

temperature = input ("Скільки зараз градусів на вулиці? ")

if temperature <= -10:
   print("Одягаємо дуже теплий одяг")
elif temperature > -10 and temperature <= 5:#else if
   print("Одягаємо теплий одяг")
elif temperature > 5 and temperature <= 16:
   print("Вдягаємось легко: кофта сорочка кеди легкі штанці ")
else:
   print("Вдягаємось по літньому: шорти футболка сандалі ")

print("Виходимо на вулицю")

# Оператори об'єднання - and, or -обєднують логічні вирази
print(f"True and True = {True and True}")
print(f"True and False = {True and False}")
print(f"False and True = {False and False}")
print(f"False and False = {False and True}")

print()

print(f"True or True = {True or True}")
print(f"True or False = {True or False}")
print(f"False or True = {False or True}")
print(f"False or False = {False or False}")

print()

# not-інвертує значення bool
print(f"not True = {not True}")
print(f"not False = {not False}")
is_raining = input("Чи іде зараз дощ? (так/ні) ")

if is_raining == 'так':
    print("Беремо парасолю!")

'''
# is_cold = input("Чи зараз холодно? (так/ні)")

# if is_cold == 'так':
#     print('Вдягаємо теплий одяг')
# else:
#     print('Вдягаємо легкий одяг')
'''

temperature = int(input("Скільки зараз градусів на вулиці? "))

if temperature <= -10:
    print('Вдягаємось дуже тепло: рукавички, термобілизна, зимова шуба, зимові штанці, черевики')
elif temperature > -10 and temperature <= 5: # else if
    print('Вдягаємо тепло: куртка, теплі штанці, теплі кросівки')
elif temperature > 5 and temperature <= 16:
    print('Вдягаємось легко: кофта, сорочка, кеди, легкі штанці')
else:
    print("Вдягаємось по-літньому: футболка, шорти, шкльопки і на море!")

boolean= bool (0) #False
print(bool(0)) #False
print(bool(0.0)) #False
print(bool("")) #False

something=None
print( bool(something)) #False
print(bool(10))#True
print(bool(-6.8))#True
print(bool("Hello"))#True


#Калькуляторю Користувач вводить два числа та обирає операцію (+-*/)
number1 =float(input("Введіть перше число: "))
number2 =float(input("Введіть друге число: "))

operation =input("Оберіть операцію (+ - * /): ")

if operation == "+":
   print(f"{number1} + {number2} = {number1 + number2}")
elif operation == "-":
   print(f"{number1} - {number2} = {number1 - number2}")
elif operation == "*":
   print(f"{number1} * {number2} = {number1 * number2}")
elif operation == "/":
   if number2 == 0
   print("Не можна ділити на нуль!")
   if number2 != 0:
       print(f"{number1} / {number2} = {number1 / number2}")
   else:
       print("Некоректна операція")


if number % 2 == 0:
   print()