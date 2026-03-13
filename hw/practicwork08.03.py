import random

def power(a, n):
    if n == 0:
        return 1
    return a * power(a, n - 1)


def leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def days_in_month(month, year):
    days = [31, 28 + leap_year(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return days[month - 1]


def date_to_days(d, m, y):
    days = d
    for year in range(1, y):
        days += 366 if leap_year(year) else 365
    for month in range(1, m):
        days += days_in_month(month, y)
    return days


def date_diff(d1, m1, y1, d2, m2, y2):
    return abs(date_to_days(d1, m1, y1) - date_to_days(d2, m2, y2))


def min_sequence(arr, i=0, min_pos=0, min_sum=None):
    if i > len(arr) - 10:
        return min_pos
    s = sum(arr[i:i+10])
    if min_sum is None or s < min_sum:
        return min_sequence(arr, i + 1, i, s)
    return min_sequence(arr, i + 1, min_pos, min_sum)


nums = [random.randint(1, 100) for _ in range(100)]

print(power(2, 5))
print(date_diff(1, 3, 2024, 13, 3, 2024))
print(min_sequence(nums))
