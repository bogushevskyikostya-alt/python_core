score = int(input("Введіть бал за іспит (0–100): "))

if score < 0 or score > 100:
    print("Помилка: бал має бути від 0 до 100")
elif score >= 90:
    print("Відмінно")
elif score >= 70:
    print("Добре")
elif score >= 50:
    print("Задовільно")
else:
    print("Незадовільно")

salary = float(input("Введіть заробітну плату: "))
experience = float(input("Введіть стаж роботи (в роках): "))

if experience < 1:
    print("Премія не передбачена")
elif experience < 3:
    print("Премія:", salary * 0.05)
elif experience < 5:
    print("Премія:", salary * 0.10)
else:
    print("Премія:", salary * 0.15)
num = input("Введіть чотиризначне число: ")

if len(num) != 4 or not num.isdigit():
    print("Помилка: число не чотиризначне")
else:
    s = int(num[0]) + int(num[1]) + int(num[2]) + int(num[3])

if s % 2 == 0:  
    print("Сума цифр парна")  
else:  
    print("Сума цифр непарна")

num = input("Введіть шестизначне число: ")

if len(num) != 6 or not num.isdigit():
    print("Помилка: число не шестизначне")
else:
    s1 = int(num[0]) + int(num[1]) + int(num[2])
s2 = int(num[3]) + int(num[4]) + int(num[5])

if s1 == s2:  
    print("Число щасливе")  
else:  
    print("Число нещасливе")

num = input("Введіть шестизначне число: ")

if len(num) != 6 or not num.isdigit():
    print("Помилка: число не шестизначне")
else:
    new_num = num[5] + num[4] + num[2] + num[3] + num[1] + num[0]
print("Результат:", new_num)
print("Задовільно")
print("Незадовільно")