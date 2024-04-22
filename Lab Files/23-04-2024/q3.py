
# WAP to calculate without using library function number of days between two dates
# (Hint : think about leap years between those dates)

def is_leap_year(year):
    """
    Function to check if a year is a leap year.
    Leap years are divisible by 4, but not by 100 unless they are also divisible by 400.
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(month, year):
    """
    Function to return the number of days in a given month of a given year.
    """
    if month in {1, 3, 5, 7, 8, 10, 12}:
        return 31
    elif month in {4, 6, 9, 11}:
        return 30
    elif is_leap_year(year):
        return 29
    else:
        return 28

def days_between_dates(start_date, end_date):
    """
    Function to calculate the number of days between two dates.
    """
    start_year, start_month, start_day = map(int, start_date.split('-'))
    end_year, end_month, end_day = map(int, end_date.split('-'))

    total_days = 0
    # Calculate days for years in between
    for year in range(start_year, end_year):
        if is_leap_year(year):
            total_days += 366
        else:
            total_days += 365

    # Calculate days for remaining months in start year
    for month in range(start_month, 13):
        total_days += days_in_month(month, start_year)
    total_days -= start_day

    # Calculate days for months in end year
    for month in range(1, end_month):
        total_days += days_in_month(month, end_year)
    total_days += end_day

    return total_days

# Example usage:
start_date = "2024-01-01"
end_date = "2024-12-31"
print("Number of days between", start_date, "and", end_date, ":", days_between_dates(start_date, end_date))
