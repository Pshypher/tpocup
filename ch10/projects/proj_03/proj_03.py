# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 14:19:25 2018

@author: Pshypher
"""
from operator import itemgetter

# naming protocol
#   variables with suffix "interval" is a list
#   variables with suffix "values" are also lists

# constants
HEADINGFIRSTCOLUMN = "Date"
HIGHDIFFERENCE = "Largest difference"
LOWDIFFERENCE = "Smallest difference"
HIGHCHANGE = "Greatest change"
LOWCHANGE = "Smallest change"
SLOPEHIGH = "High slope"
SLOPELOW = "Low slope"
DATE = "Date"
DIFFERENCE = "Last week difference"
CHANGE = "Last week change"
SLOPE = "Last week slope"

interval = 13

def read_file(file_obj) -> list:
    '''Reads each line of file_obj,gets the date and final adjusted index 
    values, return a list of lists, each nested list contains a (date,
    adj_close) tuple for each week during a 13-week interval.Thus each nested
    list is at contains at most 13 tuples.'''
    all_13_weeks_interval = [[]]    # initialize list of lists
    index = 0    
    
    for line_str in file_obj:
        if line_str[:4] == HEADINGFIRSTCOLUMN:
            continue
        line_str = line_str.strip()
        line_list = line_str.split(',')
        date_str,adj_close_float = line_list[0],float(line_list[-2])
        # partition into seperate list of 13 week intervals
        if len(all_13_weeks_interval[index]) < interval:
            all_13_weeks_interval[index].append((date_str,adj_close_float))
        else:
            index += 1
            all_13_weeks_interval.append([])
            all_13_weeks_interval[index].append((date_str,adj_close_float))
    # return all of the list containing a 13-week interval of stock transactions
    return all_13_weeks_interval

def get_max_min_difference(all_13_weeks_interval: list) -> tuple:
    '''Calculates the greatest and smallest difference of the adjusted final
    index value of each of the 13-week intervals. Returns a tuple of the 
    greatest difference and the smallest difference.'''
    # initialize variables as empty lists for both the
    max_adj_values = []   # maximums of each 13 week intervals and
    min_adj_values = []   # corresponding minimum of each of the 13 week
                                # intervals
    for thirteen_week_interval in all_13_weeks_interval:
        date,max_adj_float = max(thirteen_week_interval,key=itemgetter(1))
        date,min_adj_float = min(thirteen_week_interval,key=itemgetter(1))
        max_adj_values.append(max_adj_float)
        min_adj_values.append(min_adj_float)
        
    # calculate the difference between the maximum and minimums of the final
    # adjusted value for each 13 week interval and return the greatest and 
    # smallest difference during the entire period
    difference_list = []
    for i in range(len(all_13_weeks_interval)):
        difference_float = max_adj_values[i] - min_adj_values[i]
        difference_list.append(difference_float)
        
    # return greatest and smallest difference
    return max(difference_list),min(difference_list)

def get_max_min_change(all_13_weeks_interval: list) -> tuple:
    '''Calculates the largest and smallest change of the adjusted final index
    value for all of the 13-week intervals. Returns a tuple of the largest and
    smallest change for the entire period per 13-week intervals.'''
    change_per_13_week_list = []
    
    for thirteen_week_interval in all_13_weeks_interval:
        date_week_1,adj_val_week_1 = thirteen_week_interval[0]
        date_week_13,adj_val_week_13 = thirteen_week_interval[-1]
        change_float = adj_val_week_13 - adj_val_week_1
        change_per_13_week_list.append(change_float)
    # return the largest and smallest change
    return max(change_per_13_week_list),min(change_per_13_week_list)

def calculate_slope(date_adj_values_pairs: list) -> float:
    '''Find the linear least squares fit of the data of the adjusted final 
    index values in date_adj_values_list.'''
    # formula for calculating slope is given as
    # slope = (n*s - p*q) / (n*r - p*p)
    n = len(date_adj_values_pairs)
    y_list = [adj_value for date,adj_value in date_adj_values_pairs]
    x_list = list(range(n))
    product_xy_list = [x_list[i]*y_list[i] for i in range(n)]
    x_square_list = [num*num for num in x_list]
    # find variables p,q,r and s
    p = sum(x_list)
    q = sum(y_list)
    r = sum(x_square_list)
    s = sum(product_xy_list)
    
    slope = (n*s - p*q) / (n*r - p*p)
    
    return slope

def get_lines_of_least_square_fit(all_13_weeks_interval: list) -> list:
    '''Calculates the slope of the adjusted final index value per 13-week
     interval.Return a list of floating point values.'''
    slopes_list = []
    
    for thirteen_week_list in all_13_weeks_interval:
        slopes_list.append(calculate_slope(thirteen_week_list))
    
    return slopes_list

def adj_values_latest_week(daily_stock_trans_file) -> list:
    '''Reads the daily stock transaction file and returns a list of (date, 
    adj_value) pair for the previous 7 days.'''
    all_days_list = []
    for line_str in daily_stock_trans_file:
        if line_str[:4] == HEADINGFIRSTCOLUMN:
            continue
        line_list = line_str.strip().split(',')
        date_str,adj_close_float = line_list[0],float(line_list[-2])
        all_days_list.append((date_str,adj_close_float))
    
    all_days_list.reverse()
    current_week_list = all_days_list[:7]
    return current_week_list

def report_result(result_dict: dict) -> None:
    """Displays the results of the analysis of the stock transaction."""
    
    print("\nTwenty years of S&P 500 in 13-week intervals.\n")
    print("max and min difference between high and low values in 13 weeks: \
{:.2f} {:.2f}".format(result_dict[HIGHDIFFERENCE],result_dict[LOWDIFFERENCE]))    
    print("max and min change from first week to 13th week: {:.2f} \
{:.2f}".format(result_dict[HIGHCHANGE],result_dict[LOWCHANGE]))
    print("max and min slope of line fit to data over 13 weeks: {:.2f} \
{:.2f}".format(result_dict[SLOPEHIGH],result_dict[SLOPELOW]))
    print("latest week difference, change, slope, {0:s}: {1:.2f} {2:.2f} \
{3:.2f}".format(result_dict[DATE],result_dict[DIFFERENCE],result_dict[CHANGE],
result_dict[SLOPE]))
    
        
def main():
    stock_trans_per_week_file = open("^GSPC-weekly.csv", 'r')
    daily_stock_trans_file = open("^GSPC-daily.csv", 'r')
    all_13_weeks_interval = read_file(stock_trans_per_week_file)
    result_dict = {}
    # fetch the stock transaction for last-week
    last_week_list = adj_values_latest_week(daily_stock_trans_file)
    
    # calculate the greatest, smallest difference, the greatest, smallest
    # change, and the largest and smallest slope of the stock transactions
    # per 13 week interval
    result_dict[HIGHDIFFERENCE],result_dict[LOWDIFFERENCE] = \
    get_max_min_difference(all_13_weeks_interval)
    result_dict[HIGHCHANGE],result_dict[LOWCHANGE] = get_max_min_change(
            all_13_weeks_interval)
    slopes_list = get_lines_of_least_square_fit(all_13_weeks_interval) 
    result_dict[SLOPEHIGH] = max(slopes_list)
    result_dict[SLOPELOW] = min(slopes_list)
    
    # calculate the difference,change and slope for last week
    # difference
    date_high,high_adj_value_flt = max(last_week_list,key=itemgetter(1))
    date_low,low_adj_value_flt = min(last_week_list,key=itemgetter(1))
    result_dict[DIFFERENCE] = high_adj_value_flt - low_adj_value_flt
    # change
    result_dict[DATE],day1_adj_value_flt = last_week_list[0]
    day7,day7_adj_value_flt = last_week_list[-1]
    result_dict[CHANGE] = day7_adj_value_flt - day1_adj_value_flt
    # slope
    result_dict[SLOPE] = calculate_slope(last_week_list)
    
    # display the results
    report_result(result_dict)
    
if __name__ == "__main__":
    main()