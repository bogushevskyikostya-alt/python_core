def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)


def is_symmetric(lst, left=0, right=None):
    if right is None:
        right = len(lst) - 1
    if left >= right:
        return True
    if lst[left] != lst[right]:
        return False
    return is_symmetric(lst, left + 1, right - 1)


print(gcd(48, 18))
print(sum_digits(123))

a = [67, 50, 32, 20, 12]
if is_symmetric(a):
    print("Список симетричний")
else:
    print("Список не симетричний")