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
    """Finds three words which can be spelt the same except for their
        first two letters which can be sw, tw, or wh. """
    
    start_sw, end_sw = find_range_of_character('sw', word_list)
    start_tw, end_tw = find_range_of_character('tw', word_list)
    start_wh, end_wh = find_range_of_character('wh', word_list)
    
    for i in range(start_sw, end_sw):
        for j in range(start_tw, end_tw):
            for k in range(start_wh, end_wh):
                if word_list[i][2:]==word_list[j][2:] and \
                   word_list[j][2:]==word_list[k][2:]:
                    print(word_list[i], word_list[j], word_list[k])
                    

def find_range_of_character(sub_str, word_list):
    """Finds the index where a two character long substring begins in a 
        lexicograhically sorted word_list. Returns the start and end
        range of the character."""
    
    i = 0
    while word_list[i][:2]!=sub_str:
        i+=1
    start = i
    while word_list[i][:2]==sub_str:
        i+=1
    end = i
        
    return start, end
        
word_list = get_word_list()
puzzle(word_list)
