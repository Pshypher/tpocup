# Read data of the release year of the state-specific quarters from
# the file into a list of lists

def get_quarters_release_year(quarters_file) -> list:
    '''Reads in the file holding the state specific quarters and their release
        year. Stores each state released within the same year in a list. Returns
        a list of list'''
    
    state_quarters_list = []
    year_list = []
    for line_str in quarters_file:
        line_str = line_str.strip()
        # skip the first line
        if line_str[:3] == "The":
            continue
        try:
            year = int(line_str)
            state_quarters_list.append(year_list)
            year_list = []
            continue
        except ValueError:
            year_list.append(line_str)
            
    state_quarters_list[:1] = []
    return state_quarters_list
        
# Print the names of the states in the order of release of their quarters.
# Also print the year along with the names
def display_state_order_by_release_year(quarters: list) -> None:
    '''Displays the state in order of the release year of their quarters.'''
    year = 1999
    print("{:<15s} {:>4s}".format("States", "Year"))
    print('-'*20)
    for i, states in enumerate(quarters):
        for state in states:
            print("{:<15s} {:>4d}".format(state, year+i))
    
# Print the names of the states in increasing order of the length of their
# names. Also print the year along with the names
def display_state_order_by_length(quarters: list) -> None:
    '''Displays the states in increasing order of length of their names.'''
    states_list = order_state_quarters_by_length(quarters)
    print("{:<15s} {:>4s}".format("State", "Year"))
    print('-'*20)
    for state in states_list:
        print("{:<15s} {:>4d}".format(state[1],state[2]))
        
def order_state_quarters_by_length(quarters: list) -> list:
    '''Order the states in the list by the length of each state. Returns a list
        of tuples, each tuple containing the length of characters of a
        state_str, the state and release year of the quarter for the state.'''
    year = 1999
    state_year_list = [(len(state), state, year+i) for i, states in enumerate(
        quarters) for state in states]
    state_year_list.sort()
    return state_year_list

def print_states_for_quarters_release_year(quarters: list, year: int) -> None:
    '''Displays the states that released their quarters within that <year>.'''
    
    print("States that released their quarter during the year", year)
    print('-'*55)
    
    start_year = 1999
    states_list = quarters[year-start_year]
    for state in states_list:
        print(state)
    


def main():
    # Prompt user for file_name
    file_name = input("Enter name of file: ")
    valid_input = False
    while not valid_input:
        try:
            quarters_file = open(file_name, 'r')
            valid_input = True
        except IOError:
            print("File {:s} not found.".format(quarters_file))
            file_name = input("Enter name of file: ")

    quarters_list = get_quarters_release_year(quarters_file)
    
    print('\n')
    display_state_order_by_release_year(quarters_list)
    
    print('\n')
    display_state_order_by_length(quarters_list)

    # Prompt for a year and print all the quarters issued that year.
    print()
    year_str = input("Enter a release year for state specific quarters: ")
    valid_input = False
    
    while not valid_input:
        try:
            year_int = int(year_str)
            if year_int >= 1999 and year_int <= 2008:
                print()
                print_states_for_quarters_release_year(quarters_list,
                                                         year_int)
                valid_input = True
            else:
                print("No quarters were released during {:4d}.".format(year_int))
                year_str = input("Enter a release year for state specific quarters: ")
        except ValueError:
            print("The year should be entered in as an integer.")
            year_str = input("Enter a release year for state specific quarters: ")