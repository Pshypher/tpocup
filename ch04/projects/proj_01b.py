#1. Program designed to simulate a board-game of Mastermind
#2. Prompt for a color code of characters "ABCEDF" from a code-maker
#3. Validate the color code given by the code-master so that it contains only 
  # chars "ABCDEF"
#4. Prompt the code-breaker for a guess of color code provided by the codemaster
#5. If the code-breaker enters a valid color code
  # check each color entered by the code-breaker against the color code
  # from the code-master
        #6. If a color code from the code-breaker exists in the color code chars
          # of the code-master and is in the same position as that of the code
          # set by the code-master
            #7. Concatenate "black" to feedback_str
        #8. Otherwise if the color code exists in the code-master color code
          # but appears in the wrong order
            #9. Concatenate "white" to feedback_str
        #10. If the color code doesn't appear in the code-master color code
            #11. Add "none" to the feedback to be displayed to the code-breaker
    #12. Display the feedback to the code-breaker
       # e.g. "black-none-white-white"
    #13. Steps 4-12 are repeated until the code-breaker figures out the colors 
       # and their positions.
    #14. Halt the execution of the program when the code-breaker enters a color
       # code that matches the color code of that set by the code-master in both
       # color and order, or when the code-breaker has made a total of
       # 12 failed attempts
#15. If the code-breaker guesses correctly the color code, he wins, otherwise a
   # a loss is recorded for the code-breaker after 12 failed attempts

import random

COLORS = "ABCDEF"
CODE_LENGTH = 4
MAX_ATTEMPTS = 12
SINGLE_OCCURENCE = 1

codemaker_seq = ""
index = random.randrange(0, len(COLORS))

while len(codemaker_seq) < CODE_LENGTH:
    if COLORS[index] not in codemaker_seq:
        codemaker_seq +=    COLORS[index]
    index = random.randrange(0, len(COLORS))

failed_attempts = 0
history = ""

codebreaker_seq = input("Guess: ")
codebreaker_seq = codebreaker_seq.upper()

while failed_attempts < MAX_ATTEMPTS:
    # Validate color code entered by the code-breaker
    valid_color_code = False
    while not valid_color_code:
        for i, ch in enumerate(codebreaker_seq):
            if ch not in COLORS:
                print('guess contains a character outside the color code "ABCDEF"')
                codebreaker_seq = input("Guess: ")
                codebreaker_seq = codebreaker_seq.upper()
                break
            elif codebreaker_seq.count(ch) > SINGLE_OCCURENCE:
                print("no repeated color codes, try again")
                codebreaker_seq = input("Guess: ")
                codebreaker_seq = codebreaker_seq.upper()
                break
        else:
            if i != CODE_LENGTH-1:   
                print("guess must have a length of 4, try again")
                codebreaker_seq = input("Guess: ")
                codebreaker_seq = codebreaker_seq.upper()
            else:
                valid_color_code = True

    feedback_str = ""
    # Compare each character of the guess from a code-breaker
    # with the color code of the code-maker
    for i, ch in enumerate(codebreaker_seq):
        if ch == codemaker_seq[i]:
            feedback_str += "black "
        elif ch in codemaker_seq:
            feedback_str += "white "
        else:
            feedback_str += 'none '

    # Display feedback to the user
    feedback_str = feedback_str.strip()
    history += feedback_str + "\n"
    print(feedback_str)

    # Halt execution of the loop if the code-breaker guesses each color code
    # in the right order
    if feedback_str.count('black') == CODE_LENGTH:
        print()
        print("You win!!!")
        break
    else:
        failed_attempts += 1
        
    codebreaker_seq = input("Guess: ")
    codebreaker_seq = codebreaker_seq.upper()
    
if failed_attempts >= MAX_ATTEMPTS:
    print()
    print("You loose!!!")
    
print()
print("{:^24s}".format("History"))
print("{}".format('-'*24))
print(history)
