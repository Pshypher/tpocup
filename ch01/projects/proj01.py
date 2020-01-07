# Computer project #1
# prompts for a distance in rods, converts from rods to meters,
# from rods to feet, rods to miles, rods to furlongs and calculates
# the time it takes in minutes to walk the given distance (in rods)
# displays the results of the distances in rods, meters, feet, miles, furlongs
# and the time in minutes to walk the distance

METERS_PER_ROD = 5.0292
RODS_PER_FURLONG = 40
METERS_PER_MILE = 1609.34
METERS_PER_FT = 0.3048
AVERAGE_WALKING_SPEED = 3.1     # in units of miles per hour
MINS_PER_HOUR = 60

# prompt user for distance in rods
distance_rods_str = input("Input rods: ")
distance_rods_flt = float(distance_rods_str)   # convert type from str to float
print("You input", distance_rods_flt, "rods.")
print()

# calculate the distance from rods to meters
distance_meters_flt = distance_rods_flt * METERS_PER_ROD

# calculate the distance from rods to feet
distance_feet_flt = distance_meters_flt / METERS_PER_FT

# calculate the distance in miles from that in rods
distance_miles_flt = distance_meters_flt / METERS_PER_MILE

# calculate the distance from rods to furlong
distance_furlongs_flt = distance_rods_flt / RODS_PER_FURLONG

# compute the time it takes in minutes to walk the given distance in rods
# between lakes
time_hour_flt = distance_miles_flt / AVERAGE_WALKING_SPEED
time_minutes_flt = time_hour_flt * MINS_PER_HOUR

# display the results of all conversions
print("Conversions")
print("Meters:", distance_meters_flt)
print("Feet:", distance_feet_flt)
print("Miles:", distance_miles_flt)
print("Furlongs:", distance_furlongs_flt)
print("Minutes to walk", distance_rods_flt, "rods:", time_minutes_flt)