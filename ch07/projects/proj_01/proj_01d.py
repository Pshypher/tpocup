# Word puzzle driver
# Assumes word_list.txt file of one word per line

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
    """ Prints a set of words, with six letters that begins with a C and 
         would have its meaning changed when the first letter is
         changed from a c to h"""
    
    for word in word_list:
        if len(word)==6 and word[0]=='c':
            print("h"+word[1:])
            
    
word_list = get_word_list()
puzzle(word_list)
