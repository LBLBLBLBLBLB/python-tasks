def is_leap(year_1):
    if year_1 % 4 == 0:
        if year_1 % 100 == 0:
            if year_1 % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(years, months):
    if months > 12 or months < 1:
        return "invalid month"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(years) and months == 2:
        return 29

    return month_days[month - 1]


year = int(input("enter year"))
month = int(input("enter month"))
days = days_in_month(year, month)
print(days)
