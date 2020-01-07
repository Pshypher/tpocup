import string

def extract_data(census_file):
    """Extract the data from the census_file whilst generating clean data.
        Returns a list of lists for each state and the results of the census
        each year the census was conducted (10 year interval between
                                            each census.)"""
    
    headers_list = ["Table","Source:","Released:","UNITED","Region","Division"]
    state_populations_list = []
    # Create inner list to hold census data for each state per 10 year interval
    # Each inner list index represent the year 0 being 1990, index 1 in 1980 etc.
    
    
    for line in census_file:
        if line[:7]==' '*7:     # Skip lines indented 7 spaces to the right
            continue
        
        # Skip each line that has a keyword appearing
        # in headers_list
        valid_census_data = True
        line_list = line.split()
        for word in line_list:
            if word in headers_list:
                valid_census_data = False
                break
            
        if valid_census_data and line_list:
            state_census_data_lst = generate_clean_data(line_list)
            # print(state_census_data_lst)
            for state in state_populations_list:
                if state_census_data_lst[0] in state:
                    state.extend(state_census_data_lst[1:])
                    break
            else:
                state_populations_list.append(state_census_data_lst)

    return state_populations_list

                
def generate_clean_data(state_census_data_lst):
    """Removes comma from numbers and selects revelant columns of the census 
        data for each state in the state_census_data_lst line. Also merges  
        multiple word state names into one whole string.
        Returns a list of values."""
    
    # Remove commas from each number in the row of state census data
    # and remove characters that are keys in the footnotes of the census
    # file.
    state_census_data_lst = remove_footnote_keys(state_census_data_lst)
    state_census_data_lst = remove_commas(state_census_data_lst)        
    state_census_data_lst = merge_multiple_state_words(state_census_data_lst)
    
    if len(state_census_data_lst) > 6:
        state_census_data_lst = [state_census_data_lst[0],
                                 int(state_census_data_lst[1]),
                                 int(state_census_data_lst[6]),
                                 int(state_census_data_lst[11])]
    else:
        state_census_data_lst = [state_census_data_lst[0],
                                 int(state_census_data_lst[1])]

    return state_census_data_lst


def remove_commas(state_census_data_lst):
    """Removes commas from each column that are numbers of the
        state_census_data_lst. Return a list"""
    for i, col_data in enumerate(state_census_data_lst):
        comma_str=','
        if comma_str in col_data and col_data[0].isdigit():
            col_data = ''.join(col_data.split(','))
            state_census_data_lst[i] = col_data
            
    return state_census_data_lst
            

def remove_footnote_keys(state_census_data_lst):
    """Removes columns that are keys in the footnotes at the bottom
        of the file. Returns a list"""
    keys_in_footnotes = ['r','*1','*2']
    
    for i, col_data in enumerate(state_census_data_lst):
        if col_data in keys_in_footnotes:
            state_census_data_lst[i:i+1] = []
    
    return state_census_data_lst


def merge_multiple_state_words(state_census_data_lst):
    """Merges two or more words in the list that comprises the word
        of a single state and replace the entire word with its invidual
        composition in the list. Returns a list."""
    if state_census_data_lst[1].isalpha() and \
       state_census_data_lst[2].isalpha():
        state_census_data_lst[:3] = [state_census_data_lst[0]+' '+ \
                                     state_census_data_lst[1]+' '+ \
                                     state_census_data_lst[2]]
    elif state_census_data_lst[1].isalpha():
        state_census_data_lst[:2] = [state_census_data_lst[0]+' '+ \
                                     state_census_data_lst[1]]
    
    return state_census_data_lst


def transform(census_data_list):
    """The list is transformed such that the census is grouped over 10 decades
        the tuples containing each state and its population are grouped in an
        inner list from 1990-1900. Return a list of list of tuples."""
    years_of_census_data = []
    for i in range(1,len(census_data_list[0])):
        year = []
        for j in range(len(census_data_list)):
            year.append((census_data_list[j][i], census_data_list[j][0]))
        years_of_census_data.append(year)
    
    return years_of_census_data

# Program designed to work with the census data from 1900 to 1990
# Displays the most sparsely populated and densely populated states
# alongside the population
census_file = open("urpop0090.txt", "r")
        
state_population_list = extract_data(census_file)   # generates a list of tuples
                                                    # containing the states and 
                                                    # the population of each state
                                                    # during a particular year
census_per_ten_year_period_lst = transform(state_population_list)

# Prompt user for year between 1900-1990
valid_year_bool = False

while not valid_year_bool:
    try:
        year_str = input("Enter census year 1900 to 1990: ")
        year_int = int(year_str)
        if year_int>=1900 and year_int<=1990:
            valid_year_bool = True
        else:
            print("Number should be an integer between 1900-1990")
    except ValueError:
        print("Only integers are allowed")
        year_str = input("Enter census year 1900 to 1990: ")
    
year_index = (1990-year_int)//10
print("Minimum:",min(census_per_ten_year_period_lst[year_index]))
print("Maximum:",max(census_per_ten_year_period_lst[year_index]))


