def max_number(a, b):
    print(max(a, b))


def check_difference(a, b):
    if abs(a - b) == 135:
        print("yes")
    else:
        print("No")


def season(month):
    if month in [12, 1, 2]:
        print("зима")
    elif month in [3, 4, 5]:
        print("весна")
    elif month in [6, 7, 8]:
        print("лето")
    elif month in [9, 10, 11]:
        print("осень")
    else:
        print("Некорректный номер месяца")


def check_numbers(a, b, c):
    if a > 10 and b > 10 and c > 10:
        print("yes")
    else:
        print("no")


def total_days(years, months):
    days = (years * 12 + months) * 29
    print(days)



