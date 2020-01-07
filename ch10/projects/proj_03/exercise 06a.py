# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 12:24:18 2018

@author: Pshypher
"""
# Unless stated otherwise, variables are assumed to be a float type
from operator import itemgetter 
import proj_03    

proj_03.interval = 7    # change the interval; group in intervals of 7 days
                        # per week 
input_file = open("^GSPC-daily.csv",'r')
# print the values of the daily stock transaction for a specific period
# to a different file
stock_trans_file = open("^GSPC-selected-period-daily.csv",'w')
# prompt user for the start date and the end date of the period whose
# stock index values are to be analyzed
start_date_str = input("Enter start date in yr-mm-dd format: ")
end_date_str = input("Enter end date in yr-mm-dd format: ")

write_bool = False
for line_str in input_file:
    line_str = line_str.strip()
    date_str = line_str[:10]
    # begin writing each line of record for the stock transactions per day to
    # to the output file until the end of specified period is reached
    if date_str == start_date_str:
        write_bool = True
    elif date_str == end_date_str:
        print(line_str, file=stock_trans_file)
        break
        
    if write_bool:
        print(line_str, file=stock_trans_file)
stock_trans_file.close()

stock_trans_file = open("^GSPC-selected-period-daily.csv",'r')
weekly_stock_trans_set = proj_03.read_file(stock_trans_file)
stock_trans_file.close()    # close file after reading in data
# calculate the greatest, smallest difference, the greatest, smallest
# change, and the largest and smallest slope of the stock transactions
# per week
largest_difference,smallest_difference = \
proj_03.get_max_min_difference(weekly_stock_trans_set)
largest_change,smallest_change = proj_03.get_max_min_change(
        weekly_stock_trans_set)
slopes_list = proj_03.get_lines_of_least_square_fit(weekly_stock_trans_set) 
largest_slope = max(slopes_list)
smallest_slope = min(slopes_list)

# calculate the difference,change and slope for the last week in the second
# half of 2008
last_week_list=(weekly_stock_trans_set[-2]+weekly_stock_trans_set[-1])[-7:]
# calculate the difference
largest_adjusted_index = max(last_week_list,key=itemgetter(1))[1]
smallest_adjusted_index = min(last_week_list,key=itemgetter(1))[1]
difference = largest_adjusted_index - smallest_adjusted_index
# calculate the change 
day_1, adjusted_value_1 = last_week_list[0]
day_7, adjusted_value_7 = last_week_list[-1]
change = adjusted_value_7 - adjusted_value_1
# determine the slope
slope = proj_03.calculate_slope(last_week_list)

# display the results of the analysis of the stock transaction."""
print("\nSecond half of 2008 S&P 500 in 7-day intervals.\n")
print("max and min difference between high and low values in 7 days: \
{:.2f} {:.2f}".format(largest_difference,smallest_difference))    
print("max and min change 1st day to 7th day: {:.2f} {:.2f}".format(
        largest_change,smallest_change))
print("max and min slope of line fit to data over 7 days: {:.2f} \
{:.2f}".format(largest_slope,smallest_slope))
print("latest week difference, change, slope, {0:s}: {1:.2f} {2:.2f} \
{3:.2f}".format(day_1,difference,change,slope))