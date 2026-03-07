def formatted_text():
    print("Don't compare yourself with anyone in this world...")
    print("If you do so, you are insulting yourself.")
    print("Bill Gates")


def odd_numbers(a, b):
    for i in range(a, b + 1):
        if i % 2 != 0:
            print(i, end=" ")
    print()


def draw_line(length, direction, symbol):
    if direction == "h":
        print(symbol * length)
    elif direction == "v":
        for _ in range(length):
            print(symbol)


def max_of_four(a, b, c, d):
    return max(a, b, c, d)


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_lucky(n):
    s = str(n)
    if len(s) != 6:
        return False
    return int(s[0]) + int(s[1]) + int(s[2]) == int(s[3]) + int(s[4]) + int(s[5])


formatted_text()
odd_numbers(1, 20)
draw_line(5, "h", "*")
draw_line(5, "v", "#")
print(max_of_four(3, 7, 2, 9))
print(is_prime(7))
print(is_lucky(123420))