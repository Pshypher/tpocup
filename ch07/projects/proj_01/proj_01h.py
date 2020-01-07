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
    """Finds a seven characters long word that consists of consecutive,
        overlapping state postal abbreviations. """
    state_list = ["AK","AL","AR","AZ","CA","CO","CT","DC","DE","FL","GA","GU",
                  "HI","IA","ID", "IL","IN","KS","KY","LA","MA","MD","ME","MH",
                  "MI","MN","MO","MS","MT","NC","ND","NE","NH","NJ","NM","NV",
                  "NY","OH","OK","OR","PA","PR","PW","RI","SC","SD","TN","TX",
                  "UT","VA","VI","VT","WA","WI","WV","WY"]
    state_list = [state.lower() for state in state_list]
 
    for word in word_list:
        if len(word)==7 and word[:2] in state_list and word[1:3] in state_list \
           and word[2:4] in state_list and word[3:5] in state_list and \
           word[4:6] in state_list and word[5:] in state_list:
            print(word)
        
word_list = get_word_list()
puzzle(word_list)
