class Student:
    def init(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        self.grades = []

    def str(self):
        return f"Студент: {self.name} {self.surname}, вік: {self.age}"

    def show_grades(self):
        if self.grades:
            print("Оцінки:", self.grades)
        else:
            print("Оцінок ще немає")

    def add_grade(self, grade):
        self.grades.append(grade)
        print("Оцінку додано")


class Car:
    def init(self, brand, model, speed, year):
        self.brand = brand
        self.model = model
        self.speed = speed
        self.year = year

    def str(self):
        return f"{self.brand} {self.model} ({self.year}), швидкість: {self.speed} км/год"

    def show_info(self):
        print(self)


# ===== МЕНЮ =====
student = None
car = None

while True:
    print("\nМеню:")
    print("1 - Створити студента")
    print("2 - Додати оцінку")
    print("3 - Показати оцінки")
    print("4 - Показати студента")
    print("5 - Створити авто")
    print("6 - Показати авто")
    print("0 - Вихід")

    choice = input("Ваш вибір: ")

    if choice == "1":
        name = input("Ім'я: ")
        surname = input("Прізвище: ")
        age = int(input("Вік: "))
        student = Student(name, surname, age)

    elif choice == "2":
        if student:
            grade = int(input("Введіть оцінку: "))
            student.add_grade(grade)
        else:
            print("Спочатку створіть студента")

    elif choice == "3":
        if student:
            student.show_grades()
        else:
            print("Студента немає")

    elif choice == "4":
        if student:
            print(student)
        else:
            print("Студента немає")

    elif choice == "5":
        brand = input("Бренд: ")
        model = input("Модель: ")
        speed = int(input("Швидкість: "))
        year = int(input("Рік: "))
        car = Car(brand, model, speed, year)

    elif choice == "6":
        if car:
            car.show_info()
        else:
            print("Авто не створено")

    elif choice == "0":
        break

    else:
        print("Невірний вибір")

        import math


class Circle:
    def init(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimetr(self):
        return 2 * math.pi * self.radius


class Rectangle:
    def init(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

    def perimetr(self):
        return 2 * (self.a + self.b)


class Triangle:
    def init(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        p = self.perimetr() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def perimetr(self):
        return self.a + self.b + self.c


# ===== МЕНЮ =====
while True:
    print("\nМеню:")
    print("1 - Коло")
    print("2 - Прямокутник")
    print("3 - Трикутник")
    print("0 - Вихід")

    choice = input("Ваш вибір: ")

    if choice == "1":
        r = float(input("Введіть радіус: "))
        c = Circle(r)
        print("Площа:", c.area())
        print("Периметр:", c.perimetr())

    elif choice == "2":
        a = float(input("Сторона a: "))
        b = float(input("Сторона b: "))
        r = Rectangle(a, b)
        print("Площа:", r.area())
        print("Периметр:", r.perimetr())

    elif choice == "3":
        a = float(input("Сторона a: "))
        b = float(input("Сторона b: "))
        c_side = float(input("Сторона c: "))
        t = Triangle(a, b, c_side)
        print("Площа:", t.area())
        print("Периметр:", t.perimetr())

    elif choice == "0":
        break

    else:
        print("Невірний вибір")

        