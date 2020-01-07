# Word puzzle driver
# Assumes word_list.txt file of one word per line
import string

def get_word_list():
    """ Return a list of words from a word_list.txt file . """
    data_file = open("3eslWordList.txt","r")
    word_list = [] # start with an empty word list
    for word in data_file: # for every word (line) in the file
        # strip off end−of−line characters and make each word lowercase
        # then append the word to the word list
        word_list.append(word.strip().lower())
    data_file.close()
    return word_list

def puzzle(word_list):
    """Finds an eight-letter word resulting from adding two pairs of doubled
        letters to the word 'rate.'"""
    letters = "rate"
    
    for word in word_list:
        if len(word)==8:
            copy_str = word
            another_str = ''    # Compose a string used to determine if the
                                # letters r,a,t,e appears in sequence
            for i, ch in enumerate(word):
                # Remove the letters r,a,t,e from a copy of the original word
                if ch in letters:
                    another_str+=ch
                    copy_str = copy_str[:i]+copy_str[i+1:]
            # Compare whats left from removing the letter r,a,t,e and
            # see if the order in which r,a,t,e appears in the word is the
            # same as it appears in the variable letters
            if copy_str[0]==copy_str[1] and copy_str[2]==copy_str[3] \
               and another_str==letters:
                print(word)
            
word_list = get_word_list()
puzzle(word_list)
