# Displays an output of a 24-clock in hours, minutes and seconds
# given the number of seconds since midnight (0 seconds)
total_seconds_str = input("Enter a number in the range of 1 to 86400: ")
total_seconds_int = int(total_seconds_str)

hours = total_seconds_int // 3600
seconds_after_nhours = total_seconds_int % 3600
minutes = seconds_after_nhours // 60
seconds_left = seconds_after_nhours % 60

print("{} sec is {} hours, {} minutes, and {} seconds".format(total_seconds_str,
                                                              hours, minutes, seconds_left))
