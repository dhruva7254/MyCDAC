
# WAP to print day of input date when given day for 1st day of that month
#     ex. input date : 16/07/2022  day of 1st day of that month : Friday
#     output : saturday

from datetime import datetime, timedelta

def find_day_of_date(input_date, day_of_1st_day):
    input_date_obj = datetime.strptime(input_date, "%d/%m/%Y")
    
    day_of_1st_day_index = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'].index(day_of_1st_day.title())
    
    day_difference = (input_date_obj.weekday() - day_of_1st_day_index) % 7
    
    input_day = (day_of_1st_day_index + input_date_obj.day - 1) % 7
    
    day_name = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][input_day]
    
    return day_name

input_date = input("Enter the input date (in DD/MM/YYYY format): ")
day_of_1st_day = input("Enter the day of the 1st day of the month: ")

day_of_input_date = find_day_of_date(input_date, day_of_1st_day)

print("Day of the input date:", day_of_input_date)
