# Program creates a string of the permutations in comma-seperated form of a 
# string of length three, which serves as the input to the function
# named "permutations"
# Unless stated otherwise, variables are of type string

def permutations(substring):
    """Returns all the permutations of a string three characters long."""
    alphanum_chars = substring[1:-1]
    set_of_str_permutations = "{"
    
    for i, char in enumerate(alphanum_chars):
        remaining_chars = alphanum_chars[:i] + alphanum_chars[i+1:]
        remaining_chars_reversed = ""
        for j in remaining_chars:   # Reverse the remaining two strings
            remaining_chars_reversed = j + remaining_chars_reversed
            
        set_of_str_permutations += (char+remaining_chars) + ' ' + \
                                  (char+remaining_chars_reversed) + ' '
    
    set_of_str_permutations = set_of_str_permutations.strip()
    set_of_str_permutations += "}"
        
    return set_of_str_permutations


# Display permutations of input string three characters long
sub_str = input("Enter a string of set three characters e.g. {ABC}: ")
while len(sub_str[1:-1]) != 3:
    print("Length of string not equals to 3")
    sub_str = input("Enter a string of set three characters e.g. {ABC}: ")
    
print(permutations(sub_str))
    