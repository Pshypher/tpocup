# Unless stated otherwise, variables are assumed to be of the type str

import string

def make_word_freq_pair(words_lst):
    """Counts the number of times a word appears in a word list.: Returns
        a list of tuples, each tuple being a pair of words and their respective
        count."""
    
    unique_words_lst = []
    count_lst = []
    # Use parallel lists to map each unique word and the frequency in
    # which they appear
    for i in range(len(words_lst)):
        if words_lst[i] not in unique_words_lst:
            unique_words_lst.append(words_lst[i])
            count_lst.append(1)
        else:
            sub = unique_words_lst.index(words_lst[i])
            count_lst[sub] = count_lst[sub] + 1
        
    # Create a list of tuples, (frequency, word) pairs 
    word_count_pairs_lst = [(count_lst[j],unique_words_lst[j])       
                            for j in range(len(unique_words_lst))]
    del unique_words_lst    # remove unique_words_lst and
    del count_lst           # count_lst from memory
    return word_count_pairs_lst

        
def make_list_of_words(file_obj):
    """Makes the list of words from a file_obj excluding punctuations and --
        characters: Return a list of words."""
    words_in_file = []
    for line in file_obj:
        words_in_file.extend(remove_punctuation_hyphen(line))
    
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
        
words_lst = make_list_of_words(gba_file)
words_and_count_tuple = make_word_freq_pair(words_lst)
words_and_count_tuple.sort()    # Sort the list using the first item in each
                                # tuple the frequency at which each unique word
                                # appears in the gettysburg address file
for count, word in words_and_count_tuple:
    print("Word:", word + ", Count:", count)