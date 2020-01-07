import string


def vowel_consonant_count(sentence_str):
    """Counts and prints the number of vowels and consonants in a sentence.
       the function returns nothing."""
    
    vowel_str = "aeiou"
    
    vowel_count = 0
    consonant_count = 0
    
    sentence_str = sentence_str.lower()
    for char in sentence_str:
        if char not in string.ascii_lowercase:
            continue
        elif char in vowel_str:
            vowel_count = vowel_count + 1
        else:
            consonant_count = consonant_count + 1
            
    print("Vowels:     {:d}\nConsonants: {:d}".format(vowel_count,
                                                      consonant_count))
        
    
        
    