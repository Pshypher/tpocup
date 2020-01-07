# Word puzzle driver
# Assumes word_list.txt file of one word per line
import os

def get_word_list(file_name):
    """ Return a set of words from a word_list.txt file . """
    if not os.path.exists(file_name):
        raise FileNotFoundError("File {} not found.".format(file_name))
        
    data_file = open(file_name,"r")
    word_set = set() # start with an empty word set
    for word in data_file: # for every word (line) in the file
        # strip off end−of−line characters and make each word lowercase
        # then append the word to the word list
        word_set.add(word.strip().lower())
    data_file.close()
    return word_set.copy()

def puzzle(word_set):
    """ Finds a set of triples, such that the root word is not an adjective
        and when an "er" or "est" is added to the end of the root word creates
         another word with an unrelated meaning to that of the root word. """
    word_list = sorted(word_set)
    for root_word in word_list:
        if root_word+'er' in word_list and root_word+'est' in word_list:
            print(root_word, root_word+'er', root_word+'est')
            

def main(file_name):
    """
    >>> main("unixWordList.txt")
    b ber best
    be beer beest
    bigg bigger biggest
    car carer carest
    div diver divest
    do doer doest
    earn earner earnest
    eld elder eldest
    further furtherer furtherest
    g ger gest
    h her hest
    high higher highest
    hinder hinderer hinderest
    ing inger ingest
    inn inner innest
    l ler lest
    lat later latest
    north norther northest
    oft ofter oftest
    p per pest
    rath rather rathest
    rev rever revest
    shi shier shiest
    te teer teest
    temp temper tempest
    upper upperer upperest
    w wer west
    y yer yest
    z zer zest
    >>> main("dictionary.txt")
    Traceback (most recent call last):
        ...
    FileNotFoundError: File dictionary.txt not found.
    >>> main("3eslWordList.txt")
    p per pest
    temp temper tempest
    """
    word_set = get_word_list(file_name)
    puzzle(word_set)
    
if __name__ =='__main__':
    import doctest
    doctest.testmod()