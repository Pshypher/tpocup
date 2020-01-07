def get_data_list(file_name, column_header, sep_char=','):
    '''Reads a file <file_name> and splits each line in the file
        on a <sep_char>, puts the data into a list that is returned.'''
    data_file = open(file_name, 'r')
    data_list = []      # start with an empty list
    for line_str in data_file:
        if column_header in line_str:   # skip line if it is the header
            continue                    # of a column
        # strip end-of-line, split on sep_char, and append items to list
        data_list.append(line_str.strip().split(sep_char))
    return data_list

def get_monthly_averages(data_list: list) -> list:
    '''Calculates the average monthly stock prices using the Date,Volume,
     and Adj Close fields in each of the list in the data_list argument.'''
    monthly_averages_list = []
    
    # starting from the first month in data_list
    initial_date = data_list[0][0]
    month_str = initial_date.split('-')[1]
    previous_month = int(month_str)  
    
    total_price,total_volume = 0,0  # initialize the total price and total
                                    # volume in a month to 0
    for day in data_list:
        
        year_str, month_str, date_str = day[0].split('-')
        year_int = int(year_str)
        month_int = int(month_str)
        
        volume_flt = float(day[-2])
        total_price += volume_flt * float(day[-1])
        total_volume += volume_flt
        average_price = total_price / total_volume
        
        # append the average_price and the date tuple to the monthly_averages_list
        # if the previous month and the present month are different
        if month_int != previous_month:
            previous_month = month_int
            monthly_averages_list.append((average_price,(month_int,year_int)))
            total_price = 0     # initialize the total price for the
                                # new month to 0
            total_volume = 0    # and the total volume too
            
    average_price = total_price / total_volume
    monthly_averages_list.append((average_price,(month_int,year_int)))
        
    return monthly_averages_list
        
def print_info(monthly_averages_list):
    '''Displays the six best (highest average price) and six worst (lowest
        average price) months for Googles's stock.'''
    # sort the list in ascending order and copy the first six monthly stock
    # price data 
    monthly_averages_list.sort()
    lowest_average_prices = monthly_averages_list[:6]
    
    # Reverse the sorted list to obtain the six best months
    monthly_averages_list.reverse()
    highest_average_prices = monthly_averages_list[:6]
    
    print()
    print("Highest average prices\n")
    print("{:<15s} {:4s} {:>6s}".format("Stock Prices", "Year", "Month"))
    print('-' * 30)
    
    for data in highest_average_prices:
        stock_price, date = data
        month, year = date
        print("{:>12.2f} {:>7d} {:>6d}".format(stock_price, year, month))
        
    print()
    
    print('\n')
    print("Lowest average prices\n")
    print("{:<15s} {:4s} {:>6s}".format("Stock Prices", "Year", "Month"))
    print('-' * 30)
    
    for data in lowest_average_prices:
        stock_price, date = data
        month, year = date
        print("{:>12.2f} {:>7d} {:>6d}".format(stock_price, year, month))

def main():
    # Parse file containing stock prices and display the six best and worst
    # months for Google's stocks; data obtained from https://finance.yahoo.com
    data_list = get_data_list("table.csv", "Date")
    monthly_average_list = get_monthly_averages(data_list)
    print_info(monthly_average_list)
    
main()