# Unless otherwise stated, variables are of the list data type

import random
import string

def scramble_letters(word_str):
    """Scramble the letters in the middle of the string argument word. Returns
         a string which is the original word with the order of the letters  
        in between the first and last characters scrambled."""
    
    chars = list(word_str)
    # Seperate the first,last and character between
    first_char_str, last_char_str, chars_between = extract_chars(chars)
    
    # Two empty parallel lists assigned to the variables punc_chars and
    # punc_positions holds each punctuation char and its index if found 
    # in the middle of the chars_between list.
    punc_chars, punc_positions = [],[]
    for i, char in enumerate(chars_between):
        if char in string.punctuation:
            punc_positions.append(i)
            punc_chars.append(char)
            chars_between[i:i+1] = []
            
    # Change the order of the characters in between at random 
    random.shuffle(chars_between)
    # Insert each punctuation back into its original index
    for j in range(len(punc_chars)):
        chars_between.insert(punc_positions[j], punc_chars[j])
        
    # Add the first and last characters back to the front and rear of
    # the list of characters in between
    chars = [first_char_str]+chars_between+[last_char_str]
    
    return ''.join(chars)


def extract_chars(characters):
    """Seperates the first character, the last character(s) and the characters
        in between the first and last character(s). Returns a tuple of two
        strings and a list."""
    
    chars_at_end = ''   # Initialize empty string to keep characters at the end
                        # of the list of characters
    # From the end of the list of characters
    for i in range(len(characters)-1,0,-1):
        # Add the punctuations at the end of the list to chars_at_end
        if characters[i] in string.punctuation: 
            chars_at_end = characters[i] + chars_at_end
        else:
            chars_at_end = characters[i] + chars_at_end
            characters[i:] = []     # Slice of the last alphanumeric character
            break                   # along with non alphanumeric chars at the
                                    # end of the list
    first_char = characters[0]
    return first_char, chars_at_end, characters[1:]

def getWordString():
    """Reads in the content of a file into a whole string of words.
        Returns the entire string of words."""
    dataFile = open("someFile.txt", "r")
    wordString = ''             # start with an empty string of words
    for line in dataFile:
        wordString += line      # add each line of words to the word string
    dataFile.close()
    return wordString
    
    
# Program designed to scramble the letters in between each word. The first and
# last letters are reserved at the same position as the original word before
# scrambling

text = "Four score and seven years ago \
our fathers brought forth \
on this continent a new nation,"

word_list = getWordString().split()
for i in range(len(word_list)):
    word_list[i].strip()
    # Scramble only the words 4 characters or longer
    word_str = scramble_letters(word_list[i]) if len(word_list[i])>=4 \
           else word_list[i]
    word_list[i] = word_str
    
scrambled_text = ' '.join(word_list)
print(scrambled_text)