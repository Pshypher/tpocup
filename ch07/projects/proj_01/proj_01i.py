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
    """Finds a word that uses i,j,t,and x exactly once . """
    
    multiple_stroke_letters = ['i','j','t','x']
    for word in word_list:
        if word.count('i')==1 and word.count('j')==1 and word.count('t')==1 \
           and word.count('x')==1:
            print(word)
            break


word_list = get_word_list()
puzzle(word_list)
