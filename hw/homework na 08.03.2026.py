def formatted_text():
    print("Don't compare yourself with anyone in this world...")
    print("If you do so, you are insulting yourself.")
    print("Bill Gates")


def even_numbers(a, b):
    for i in range(a, b + 1):
        if i % 2 == 0:
            print(i, end=" ")
    print()


def draw_square(size, symbol, filled):
    for i in range(size):
        if filled:
            print(symbol * size)
        else:
            if i == 0 or i == size - 1:
                print(symbol * size)
            else:
                print(symbol + " " * (size - 2) + symbol)


def count_digits(number):
    return len(str(abs(number)))


def is_palindrome(number):
    s = str(number)
    return s == s[::-1]


formatted_text()
even_numbers(2, 10)
draw_square(5, "*", True)
draw_square(5, "*", False)
print(count_digits(3456))
print(is_palindrome(123321))
print(is_palindrome(421987))