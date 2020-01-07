# Our implementation of the find function. Prints the index where
# the target  is found; a failure message, if it isn't found.
# This version only searches for a single character.

river = 'Mississippi'
target = input('Input a character to find: ')
found = False
for index, letter in enumerate(river):          # for each index
    if letter == target:                        # check if the target is found
        found = True                            # set the found flag to true if the 
                                                # character exists in the string
        print("Letter found at index: ", index)     # if so, print the index
        #break
else:
    if not found:
        print('Letter', target, 'not found in', river)
    
