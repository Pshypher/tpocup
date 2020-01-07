# Program designed to create a list of words from a sentence
# punctuations aren't allowed to be attached to a word in the list
import string

sentence = input("Enter a phrase, clause or sentence: ")

# split the entire string on each whitespace character
words_lst = sentence.split()
i = 0

# Using the while loop 
while i < len(words_lst):
    # replace each character in the word with an empty string if it is
    # a punctuation
    j = 0
    while j < len(words_lst[i]):
        if words_lst[i][j] in string.punctuation:
            words_lst[i] = words_lst[i].replace(words_lst[i][j], '')
            continue
        j = j + 1
        
    i = i + 1
            
print("Words:", words_lst)
