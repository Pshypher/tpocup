# A for loop that prints when
# "alphebetical" is the input
word_str = "alphebetical"
count_int = 1

for letter in word_str:
    if not count_int % 3:
        print(letter, end='')    
    count_int = count_int + 1