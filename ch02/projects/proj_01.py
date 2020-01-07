# program written to determine how many total grains of wheat a local
# ruler paid the man who invented chess

# number of grains = 1
# while the number of squares on a chess board is less than 64
#   multiply the number of grains by a factor of 2
# display the total number of grains offered to the inventor

# unless stated otherwise, variables are assumed to be of type int

WEIGHT_MG = 50   # milligram
WEIGHT_KG = 0.00005 # kilogram
WHEAT_DENSITY = 790 # kilogram per cubic meter
CHESS_BOARD_SQUARE_SIZE = 64

number_of_grains = 1
num_squares = 1


while num_squares < CHESS_BOARD_SQUARE_SIZE:
    number_of_grains = number_of_grains * 2
    num_squares = num_squares + 1
    
print("Number of grains:", number_of_grains)

# compute the total weight of all the wheat grains paid to the man who
# invented chess
total_weight_mg = number_of_grains * WEIGHT_MG
total_weight_kg_flt = number_of_grains * WEIGHT_KG
print("Total Weight (kg):", total_weight_kg_flt)

# Density of a grain of wheat is 790 kilogram per cubic meter
# Kaduna state is 46,053,000,000 square meters
area_str = input("Enter the area of a region (in square meters): ")
area = int(area_str)

vol_flt = total_weight_kg_flt / WHEAT_DENSITY
depth_flt = vol_flt / area
print("Depth of grain covering a region of", area, "square meters is", \
      depth_flt, "meters.")