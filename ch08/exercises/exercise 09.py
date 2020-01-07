def anagrams(one_str: str, other_str: str) -> bool:
    '''Compares to strings to see if they are both anagrams.'''
    
    # Sort both strings
    one_list = sorted(one_str)
    other_list = sorted(other_str)
    
    # Convert the sorted characters in both lists to a string
    one_str = ''.join(one_list)
    other_str = ''.join(other_list)
    
    # Check that both strings are equal
    return one_str == other_str


def main():
    # Prompt user for both strings to be compared
    one_str = input("Enter a string of words: ")
    other_str = input("Enter another word, an anagram of the first word: ")
    
    anagrams_bool = anagrams(one_str, other_str)
    
    if anagrams_bool:
        print("Both {} and {} are anagrams.".format(one_str, other_str))
    else:
        print("{} and {} aren't anagrams.".format(one_str, other_str))
        