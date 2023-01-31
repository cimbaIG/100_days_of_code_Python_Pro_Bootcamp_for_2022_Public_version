def is_leap(year):
    """Checks for a leap year."""
    if year % 100 == 0 and year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False

def days_in_month(year, month):
    """For a given year and month, 
    it returns number of days."""
    if month > 12 or month < 1:
        return "Invalid input."
    else:  
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if is_leap(year) == True:
            month_days[1] = 29
            return month_days[month - 1]
        else:
            return month_days[month - 1]

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)