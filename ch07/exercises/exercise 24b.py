# Program designed to create a list of words from a sentence
# punctuations aren't allowed to be attached to a word in the list
import string

sentence = input("Enter a phrase, clause or sentence: ")

# split the entire string on each whitespace character
words_lst = sentence.split()

# for each word in the word list
for i in range(len(words_lst)):
    # replace each character in the word with an empty string if it is
    # a punctuation
    for ch in words_lst[i]:
        if ch in string.punctuation:
            words_lst[i] = words_lst[i].replace(ch, '')
            
print("Words:", words_lst)