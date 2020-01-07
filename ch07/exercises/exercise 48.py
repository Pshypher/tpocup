# Unless stated otherwise, variables are assumed to be of the type str

import string
        
def make_word_pairs(file_obj):
    """Makes a list of tuples that consist of a pair of two words from a 
        file_obj excluding punctuations and -- characters: Return a
        list of word pairs."""
    words_in_file = []
    for line in file_obj:
        words = remove_punctuation_hyphen(line)
        for i in range(0,len(words)-1,2):
            words_in_file.append((words[i], words[i+1]))
        else:
            if len(words) > 0 and words[i] != words[-1]:
                words_in_file.append((words[-1],))
    
    return words_in_file


def remove_punctuation_hyphen(S):
    """Removes punctuation and -- characters from S. Returns a list of words
        without punctuation and -- characters."""
    words_lst = S.split()
    i = 0
    while i < len(words_lst):
        if words_lst[i] == '--':
            words_lst[i:i+1] = []   # remove -- from list of words
            continue
        else:
            for ch in words_lst[i]: # for each character in a word
                # remove the character if it happens to be a punctuation symbol
                if ch in string.punctuation:    
                    words_lst[i] = words_lst[i].replace(ch, '')
        i = i+1
        
    return words_lst


# Prompt user for the name of the file, re-attempt each time the user enters
# a file that does not exist

filename = input("Enter the name of file: ")

found = False
while not found:
    try:
        gba_file = open(filename, 'r')
        found = True
    except IOError:
        print("Wrong file name provided as input.")
        filename = input("Enter the name of file: ")
        
word_pairs = make_word_pairs(gba_file)
print()

print("Word Pairs")
print(word_pairs)