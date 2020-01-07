# Program written to calculate the total distance of the
# Voyager 1 spacecraft from the sun since September 15, 1977

current_distance_int = 16637000000    # total distance as of September 25, 2009 in miles
speed = 38241    # speed in miles/hour
speed_of_rw_ms = 299792458    # speed of light in meters/second

# Prompt user for the number of days after 9/25/09
days_str = input("Number of days after 9/25/09: ")
days_int = int(days_str)

miles_per_day = speed * 24    # speed in miles/day
distance_since_ndays = days_int * miles_per_day

total_distance_miles = distance_since_ndays + current_distance_int # distance in miles
total_distance_km = total_distance_miles * 1.609344    # distance in kilometers
total_distance_AU = total_distance_miles / 92955887.6    # distance in Astronomical Units
print("Total distance of the Voyager I spacecraft", days_str, "after 9/25/09 is",
      total_distance_miles, "miles")
print("Total distance of the Voyager I spacecraft", days_str, "after 9/25/09 is",
      total_distance_km, "kilometers")
print("Total distance of the Voyager I spacecraft", days_str, "after 9/25/09 is",
      total_distance_AU, "AU")

speed_of_rw_miles_per_hr = speed_of_rw_ms / (3600 * 1609.344)    # speed of light in miles per hour 
round_trip_time = total_distance_miles / speed_of_rw_miles_per_hr
print("Round trip time for radio communication is", round_trip_time, "hours.")
