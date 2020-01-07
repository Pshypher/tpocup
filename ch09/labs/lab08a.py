import string
from operator import itemgetter


def add_word( word_map, word ):
    '''Adds a word to the dictionary word_map with an initial value 0'''
    # Associate the word with an initial value of 0 in the word_map dict
    if word and word not in word_map:
        word = word.lower()
        word_map[ word ] = 0

    # Increase the frequency(the value) of each word(the key) by 1 in
    # the word_map dict
    if word:
        word_map[ word ] += 1


def build_map( in_file, word_map ):
    '''Makes a word:count pair counting the number of occurence of
     each word from in_file and updating the dict word_map.'''
    for line in in_file:

        # Split each line into a list of words using the space character as a 
        # delimiter
        word_list = line.split()

        for word in word_list:

            # strip whitespace and punctuation characters away from each word
            # in word_list, add word to the dict, word_map
            word = word.strip().strip(string.punctuation)
            add_word( word_map, word )
        

def display_map( word_map ):
    '''Displays each word:count pair in a nicely formatted manner.''' 
    word_list = list()

    # Create a list of tuples containing the pair (word, count) from the 
    # dict word_map
    for word, count in word_map.items():
        word_list.append( (word, count) )

    # Sort word_list based on the second item in each of the tuples
    freq_list = sorted(word_list)
    freq_list.sort( key=itemgetter(1), reverse=True )

    print( "\n{:15s}{:5s}".format( "Word", "Count" ) )
    print( "-"*20 )
    for item in freq_list:
        print( "{:15s}{:>5d}".format( item[0], item[1] ) )


def open_file():
    '''Open a file to be processed. Returns a file object or None if file was
        not found.'''
    file_name = input("Enter the name of the file: ")
    try:
        in_file = open( file_name, "r" )
        
    except IOError:
        print( "\n*** unable to open file ***\n" )
        in_file = None

    return in_file


word_map = dict()
in_file = open_file()

if in_file != None:

    build_map( in_file, word_map )
    display_map( word_map )
    in_file.close()


