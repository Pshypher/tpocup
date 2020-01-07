# Program makes a list of unique letters used in a sentence; punctuations
# are not allowed in the list
# Unless stated otherwise, variables are of the type str

PUNCTUATION = ".,;?!-"
sentence = input("Enter a phrase, clause or sentence: ")
sentence_copy = sentence

# initialize an empty list for each character that appears in the sentence
chars_in_sentence_lst = []

# using a while loop iterate through the collection of chars in the string
while sentence_copy:
    # ignore characters that already appears in the list
    # characters that in the punctuation string
    if sentence_copy[0].lower() in chars_in_sentence_lst or \
       sentence_copy[0] in PUNCTUATION:
        sentence_copy = sentence_copy[1:]
        continue
    
    chars_in_sentence_lst.append(sentence_copy[0].lower())
    sentence_copy = sentence_copy[1:]
    
# display the list of characters
print("Unique list of characters:", chars_in_sentence_lst) 