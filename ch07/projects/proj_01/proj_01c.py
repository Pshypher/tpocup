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
    """ Finds words with two consecutive pronouns in them. """
    pronoun = ['thou', 'thee', 'thine', 'thy', 'i', 'me',
        'mine', 'my', 'we', 'us', 'ours', 'our', 'you', 'yours',
        'your','he','him','his', 'she', 'her', 'hers', 'it',
        'its', 'they', 'them', 'theirs', 'their']

    for i in pronoun:
        for word in word_list:
            if i in word:
                sub = pronoun.index(i)
                for j in pronoun[:sub]+pronoun[sub+1:]:
                    if i+j in word:
                        print(word)
            
word_list = get_word_list()
puzzle(word_list)