# The letters a, b, d, e, g, o, p and q all have something in common: a hole
# The function immediately below is designed to count the number of characters
# with holes and those without

# Unless stated otherwise, variables are assumed to be of the type str

alpha_with_holes_lower = 'a','b','d','e','g','o','p','q'
alpha_with_holes_upper = 'A','B','D','O','P','Q','R'
def alpha_with_and_without_holes(S):
    """Returns the number of characters with holes in S and the number
        of characters without holes in S."""
    
    with_holes = 0
    without_holes = 0
    
    for ch in S:
        if ch in alpha_with_holes_lower or ch in alpha_with_holes_upper:
            with_holes = with_holes+1
        else:
            without_holes = without_holes+1
            
    return with_holes, without_holes


# The other function below prints all the words that have two or more letters
# with holes
def words_with_two_or_more_holes(word_lst):
    """Takes in a list of words and prints the each word in the list with two
        or more holes in them. Returns None."""
    
    print("Words with two or more holes in them: ")
    for word in word_lst:
        if alpha_with_and_without_holes(word)[0] >= 2:
            print("    ", word)


# Prompt user for a sentence
sentence = input("Enter a phrase, clause or sentence: ")
list_of_words = sentence.split()
words_with_two_or_more_holes(list_of_words) # display words with 2 or more
                                            # holes in them
