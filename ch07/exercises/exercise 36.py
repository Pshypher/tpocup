# Program displays the words of sentence in reversed order
# Unless stated otherwise, variables are of the type str

def reverse(S):
    """Function reverses the order of the words in the sentence S using a for loop:
        Returns a string of the words of the sentence S in a reversed order"""
    # split the argument S on each whitespace character
    words_lst = S.split()
    # reverse the list returned by the split method
    reversed_words_lst = []
    for word in words_lst:
        reversed_words_lst = [word] + reversed_words_lst 
    # join the list seperating each word with a whitespace char
    sentence_reversed = ' '.join(reversed_words_lst)
    return sentence_reversed

# Prompt user for a sentence
sentence = input("Enter sentence: ")
# Reverse the words using a predefined function and store the result in a variable
reversed_sentence = reverse(sentence)    
# Display the reversed words of the sentence
print(reversed_sentence)                 