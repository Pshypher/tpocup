# Word puzzle driver
# Assumes word_list.txt file of one word per line

def get_word_list():
    """ Return a list of words from a word_list.txt file . """
    data_file = open("unixWordList.txt","r")
    word_list = [] # start with an empty word list
    for word in data_file: # for every word (line) in the file
        # strip off end−of−line characters and make each word lowercase
        # then append the word to the word list
        word_list.append(word.strip().lower())
    data_file.close()
    return word_list

def puzzle(word_list):
    """Finds other words that contains all the letters of memphis."""
    letters = ''.join(sorted("memphis"))
    
    for word in word_list:
        compare_str = ''
        for ch in word:
            if ch in letters:
                compare_str += ch
        compare_str = ''.join(sorted(compare_str))
        if letters==compare_str:
            print(word)            
            
word_list = get_word_list()
puzzle(word_list)
