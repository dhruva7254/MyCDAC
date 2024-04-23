
# WAP to convert input number of seconds to HH:MM:SS.

def seconds_to_hh_mm_ss(seconds):
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    
    time_string = '{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds)
    return time_string

seconds = int(input("Enter the number of seconds: "))

time_formatted = seconds_to_hh_mm_ss(seconds)

print("Formatted time:", time_formatted)
