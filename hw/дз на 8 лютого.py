while True:
   
    print("1 — а")
    print("2 — б")
    print("3 — в")
    print("4 — г")
    print("5 — д")
    print("6 — е")
    print("7 — ж")
    print("8 — з")
    print("9 — и")
    print("10 — к")
    print("0 — Выход")

    choice = input("Выбери фигуру: ")
    if choice == "0":
        print("Выход ")
        break

    n = int(input("Введи размер: "))

    # а
    if choice == "1":
        for i in range(n):
            for j in range(n):
                if i + j >= n - 1:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()

    # б
    elif choice == "2":
        for i in range(n):
            for j in range(n):
                if i >= j:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()

    # в
    elif choice == "3":
        for i in range(n):
            for j in range(n):
                if i + j <= n - 1 and j >= i:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()

    # г
    elif choice == "4":
        for i in range(n):
            for j in range(n):
                if i + j <= n - 1:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()

    # д (X)
    elif choice == "5":
        for i in range(n):
            for j in range(n):
                if i == j or i + j == n - 1:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()

    # е (песочные часы)
    elif choice == "6":
        for i in range(n):
            for j in range(n):
                if (i <= j and i + j >= n - 1) or (i >= j and i + j <= n - 1):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()

    # ж
    elif choice == "7":
        for i in range(n):
            for j in range(n):
                if j <= i:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()

    # з
    elif choice == "8":
        for i in range(n):
            for j in range(n):
                if j >= i:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()

    # и
    elif choice == "9":
        for i in range(n):
            for j in range(n):
                if i == j:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()

    # к
    elif choice == "10":
        for i in range(n):
            for j in range(n):
                if i + j == n - 1:
                    print("*", end=" ")
                else:
                    print("", end="")
            print()
    else:
        print("Неверный выбор!")