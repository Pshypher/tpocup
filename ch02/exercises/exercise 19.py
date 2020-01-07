import random
MAGIC_NUMBER = random.randint(1, 10)
guess_str = input("Enter an integer between 1 and 10: ")
guess_int = int(guess_str)
	
while True:
    if MAGIC_NUMBER == guess_int:
        break
    guess_str = input("Wrong number! Enter an integer between 1 and 10: ")
    guess_int = int(guess_str)
	
print("Correct") 
	