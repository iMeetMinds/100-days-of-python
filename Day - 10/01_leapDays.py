def is_leap_year(entered_year):
    if entered_year % 4 == 0 :
        if entered_year % 100 == 0:
            if entered_year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_months(year, month):
    month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
    if is_leap_year(year):
        month_days[1] = 29

    return month_days[month-1]

year = int(input("Enter a year : "))
month = int(input("Enter a month : "))
days = days_months(year, month)
print(days)