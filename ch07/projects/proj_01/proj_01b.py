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
    """ Finds an uncapitalized, unhyphenated word that contains all but one
        of the letters of the alphabet from l to v (lmnopqrstuv)"""
    for word in word_list:
        chars = "lmnopqrstuv"
        if '-' not in word:
            i=0
            while i<len(word):
                if word[i] in chars:
                    sub = chars.find(word[i])
                    chars = chars[:sub] + chars[sub+1:]
                i+=1
            else:
                if len(chars)==1:
                    print(word)
                    
    #pass    # filler that does nothing except put something in the suite
            
word_list = get_word_list()
puzzle(word_list)