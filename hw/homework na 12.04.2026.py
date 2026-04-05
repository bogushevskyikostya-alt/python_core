class Book:
    def init(self, title, authors, year):
        self.title = title
        self.authors = authors
        self.year = year

    def str(self):
        return f"{self.title} ({self.year}) - Автори: {', '.join(self.authors)}"


class Library:
    def init(self, name, address):
        self.name = name
        self.address = address
        self.books = []

    def str(self):
        return f"Бібліотека: {self.name}, Адреса: {self.address}"

    def show_books(self):
        if not self.books:
            print("Книг немає")
        else:
            for i, book in enumerate(self.books, 1):
                print(f"{i}. {book}")

    def add_book(self, book):
        self.books.append(book)
        print("Книгу додано")

    def remove_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print("Книгу видалено")
                return
        print("Книгу не знайдено")

    def find_by_title(self, title):
        for book in self.books:
            if title.lower() in book.title.lower():
                print(book)

    def find_by_author(self, author):
        found = False
        for book in self.books:
            if any(author.lower() in a.lower() for a in book.authors):
                print(book)
                found = True
        if not found:
            print("Нічого не знайдено")


# ===== МЕНЮ =====
lib = Library("Одеська бібліотека", "м. Одеса")

while True:
    print("\nМеню:")
    print("1 - Показати книги")
    print("2 - Додати книгу")
    print("3 - Видалити книгу")
    print("4 - Пошук за назвою")
    print("5 - Пошук за автором")
    print("0 - Вихід")

    choice = input("Ваш вибір: ")

    if choice == "1":
        lib.show_books()

    elif choice == "2":
        title = input("Назва книги: ")
        authors = input("Автори (через кому): ").split(",")
        authors = [a.strip() for a in authors]
        year = int(input("Рік: "))
        book = Book(title, authors, year)
        lib.add_book(book)

    elif choice == "3":
        title = input("Введіть назву для видалення: ")
        lib.remove_book(title)

    elif choice == "4":
        title = input("Введіть назву: ")
        lib.find_by_title(title)

    elif choice == "5":
        author = input("Введіть автора: ")
        lib.find_by_author(author)

    elif choice == "0":
        break

    else:
        print("Невірний вибір")
        