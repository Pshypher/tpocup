# Program written to English words into their Pig Latin form

# Prompt user for an english word
# Change the case of the word (lower case)
# If the user enters a word other than the string corresponding to "quit"
    # If the first character of the string is a vowel, append "way" to the end
    # of the word
    # Otherwise loop through the string to find the first occurence of a vowel
    # remove the consonants from the beginning of the word and append them to
    # end of the word. Then append "ay" to the end of the word.
    # display the pig-latin Equivalent of the English word
# Halt the program if the word "quit" is entered by the user

VOWELS = "aeiou"
QUIT = "quit"

word_str = input("Enter an english word: ")
word_str = word_str.lower()
original_str = word_str

while word_str != QUIT:
    if word_str[0] in VOWELS:
        suffix = "way"
    else:
        for ind, char in enumerate(word_str):
            if char in VOWELS:
                first_vowel_index = ind
                break
        word_str = word_str[first_vowel_index:] + word_str[:first_vowel_index]
        suffix = "ay"
        
    piglatin_str = word_str + suffix
    print("\"{}\" becomes \"{}\"".format(original_str, piglatin_str))
    
    word_str = input("Enter an english word: ")
    word_str = word_str.lower()
    original_str = word_str
    
