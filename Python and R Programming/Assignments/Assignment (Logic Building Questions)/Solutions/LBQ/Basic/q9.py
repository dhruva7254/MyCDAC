
# WAP to print calender for a month. Take how many days are there in month and starting day of the month as input
#     Ex. input no of days : 30  starting day of month : Thursday
#     Ouput :: Day wise Calender  ( just like June 2022 month)

import calendar

def print_calendar(days, starting_day):
    starting_day_index = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'].index(starting_day.title())
    
    cal = calendar.Calendar(firstweekday=0)  
    month_calendar = cal.monthdayscalendar(2024, 4)  
    
    for week in month_calendar:
        if starting_day_index > 0:
            week[:] = [0] * starting_day_index + week[:-starting_day_index]
        starting_day_index = 0
    
    print("Mon Tue Wed Thu Fri Sat Sun")
    for week in month_calendar:
        for day in week:
            if day == 0:
                print("   ", end=" ")  
            else:
                print("{:2}".format(day), end=" ")  
        print()

days = int(input("Enter the number of days in the month: "))
starting_day = input("Enter the starting day of the month: ")

print_calendar(days, starting_day)
