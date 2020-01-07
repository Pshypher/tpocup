# Word puzzle driver
# Assumes word_list.txt file of one word per line

# Unless stated otherwise, each variable is assumed to be of the str type

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
    """Finds a word that contains a,e,i,o,u in that order . """
    
    vowels = "aeiou"
    
    for word in word_list:
        vowels_in_word = ''
        for ch in word:
            if ch in vowels and ch not in vowels_in_word:
                vowels_in_word += ch
        if vowels_in_word==vowels:
            print(word)
            
word_list = get_word_list()
puzzle(word_list)
