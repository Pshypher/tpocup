# date and time (24-hour clock) in the following format MM/DD/YYYY HR:MIN:SEC
# are validated by a function and displayed in the following formats
# MM/DD/YYYY
# HR:MIN:SEC
# MM/YYYY
# and whether the time is a.m or p.m

def validate_display_datetime(datetime_str):
    MONTHS_PER_YEAR = 12
    HOURS_PER_DAY = 23
    MINS_PER_HOUR = 59
    SECS_PER_MIN = 59
    
    try:
        date_str = datetime_str[:datetime_str.find(' ')]
        time_str = datetime_str[datetime_str.find(' ')+1:]
        if int(date_str[:date_str.index('/')]) > MONTHS_PER_YEAR:
            print("Given month should lie between 1-12")
        elif int(date_str[date_str.index('/')+1:date_str.rindex('/')]) \
           > days_in_month(int(date_str[:date_str.index('/')])):
            print("Date of the month lies outside the range for the date \
                  of the month")
        elif int(time_str[:time_str.index(':')]) > HOURS_PER_DAY:
            print("Hours per day should be less than 24")
        elif int(time_str[time_str.index(':')+1:time_str.rindex(':')]) \
             > MINS_PER_HOUR:
            print("Minutes per hour should be between 0-59")
        elif int(time_str[time_str.rindex(':')+1:]) > SECS_PER_MIN:
            print("Seconds per minute is between 0-59")
        else:
            print(date_str)
            print(time_str)
            print(date_str[:date_str.index('/')]+'/'+
                  date_str[date_str.rindex('/')+1:])
            if int(time_str[:time_str.index(':')]) < 12:
                print("a.m.")
            else:
                print("p.m.")
    except TypeError:
        print("The datetime should be passed in as an argument of type str") 
    except ValueError:
        print("The datetime argument should be in the format \
MM/DD/YYYY HR:MIN:SEC e.g. 12/04/1990 13:12:12")
        
        
def days_in_month(month_int):
    """Returns the number of days in a month."""
    if month_int == 2:
        days = 28
    elif month_int == 4 or month_int == 6 or month_int == 9 or month_int == 11:
        days = 30
    else:
        days = 31
    
    return days