# Unless stated otherwise, variables are assumed to be of the type str
import string

def split_str(S):
    """Splits each the entire str S on whitespace chars, removing characters
        that are not alphanumeric: Returns a list of words in S."""
    L = []
    word = ''
    for ch in S:
        if ch in string.punctuation:
            word = word + ''
        elif ch in string.whitespace:
            L.append(word)
            word = ''
        else:
            word += ch
    else:
        L.append(word)
            
    return L

# Prompt user for input and use predefined function to split the string
sentence = input("Enter phrase, clause or sentence: ")
print(split_str(sentence))
        
    
    