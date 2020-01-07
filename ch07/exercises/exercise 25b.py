# Program makes a list of unique letters used in a sentence; punctuations
# are not allowed in the list
# Unless stated otherwise, variables are of the type str

PUNCTUATION = ".,;?!-"
sentence = input("Enter a phrase, clause or sentence: ")

# initialize an empty list for each character that appears in the sentence
chars_in_sentence_lst = []

# using a for loop iterate through the collection of chars in the string
for ch in sentence:
    # ignore characters that already appears in the list
    # characters that in the punctuation string
    if ch.lower() in chars_in_sentence_lst or \
       ch in PUNCTUATION:
        continue
    
    chars_in_sentence_lst.append(ch.lower())
    
# display the list of characters
print("Unique list of characters:", chars_in_sentence_lst) 
