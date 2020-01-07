import string
# Unless stated otherwise, each variable data type is a list

def is_palindrome(word_str: str) -> bool:
    '''Checks if the word is a palindrome.'''
    # Parameter is converted to a list
    word = list(word_str.lower())
    
    for ch in word:
        if ch not in string.ascii_letters:
            word.remove(ch)
    
    # Copy the list and reverse the order of elements in the list
    word_reverse = word[:]
    word_reverse.reverse()
    
    return word == word_reverse
    
    
def both_palindromes(one_str: str, other_str: str) -> bool:
    '''Checks if both strings are palindromes. Returns true if both
        are palindromes, false otherwise.'''
    
    return is_palindrome(one_str) and is_palindrome(other_str)


# Prompt user for two strings
one_str = input("Enter a phrase, clause or sentence: ")
other_str = input("Enter another phrase, clause or sentence: ")

if both_palindromes(one_str, other_str):
    print("Both \"{}\" and \"{}\" are palindromes.".format(one_str, other_str))
elif is_palindrome(one_str):
    print("Only \"{}\" is a palindrome.".format(one_str))
elif is_palindrome(other_str):
    print("Only \"{}\" is a palindrome.".format(other_str))
else:
    print("Neither is a palindrome.")
    
    