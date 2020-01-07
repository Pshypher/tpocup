# Calculates the number of seconds elapsed since the first second of the
# current year
# Unless stated otherwise; variables are of type int

def num_seconds_elapsed(datetime_str):
    """Takes as input a string that stores date and time in the format
    MM/DD/YYYY HR:MIN:SEC and print the number of seconds elapsed since
    01/01/YYYY 00:00:00."""
    HOURS_PER_DAY = 24
    MINS_PER_HOUR = 60
    SECS_PER_MIN = 60
    
    # Split the datetime string format into seperate date and time strings
    date_str = datetime_str[:datetime_str.find(' ')]
    time_str = datetime_str[datetime_str.find(' ')+1:]
    
    day = int(date_str[date_str.find('/')+1:date_str.rfind('/')]) # extracts date
    current_month = int(date_str[:date_str.find('/')])  # slices the month from date_str
    year = int(date_str[date_str.rfind('/')+1:]) # extracts the year from date_str
    hour = int(time_str[:time_str.find(':')]) # slices the hour from time_str
    # slice the minutes from time_str
    minutes = int(time_str[time_str.find(':')+1:time_str.rfind(':')]) 
    seconds = int(time_str[time_str.rfind(':')+1:]) # slices the seconds elapsed from time_str
    
    total_days_since_jan = 0
    month = 1
    while month < current_month:
        total_days_since_jan += days_in_month(month, year)
        month += 1
    total_days_since_jan += day-1
    secs_since_jan = total_days_since_jan * HOURS_PER_DAY * MINS_PER_HOUR * \
                         SECS_PER_MIN
    secs_since_midnite = hour * MINS_PER_HOUR * SECS_PER_MIN + minutes * \
                              SECS_PER_MIN + seconds
    total_num_seconds = secs_since_jan + secs_since_midnite
        
    print("Number of seconds elapsed since {1:s} is {0:d}".format(
        total_num_seconds, "01/01/YYYY 00:00:00"))


def days_in_month(month_int, year):
    """Returns the number of days in a month."""
    if month_int == 2:
        if is_leap_year(year):
            days = 29
        else:
            days = 28
    elif month_int == 4 or month_int == 6 or month_int == 9 or month_int == 11:
        days = 30
    else:
        days = 31
    
    return days
    
def is_leap_year(year):
    """Returns True if the year is a leap year otherwise returns False."""
    if year % 4:
        leap_year_bool = False
    else:
        if not (year % 4) and not (year % 100) and year % 400:
            leap_year_bool = False
        else:
            leap_year_bool = True
            
    return leap_year_bool
    
    
    