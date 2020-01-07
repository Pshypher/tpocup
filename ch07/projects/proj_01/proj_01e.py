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
    """Finds an uncapitalized,seven-letter word, containing just a single
        vowel that does not have the letter s anywhere within it. """
    vowels = 'aeiou'
    for word in word_list:
        if len(word)==7 and 's' not in word:
            vowel_count = 0
            for char in word:
                if char in string.punctuation:
                    break
                if char in vowels:
                    vowel_count += 1
            else:
                if vowel_count==1:
                    print(word)
                
word_list = get_word_list()
puzzle(word_list)
