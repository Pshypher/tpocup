# Program designed to read a file and insert carriage-return characters (\n)
# and write the contents of the file to a new text file that is composed of
# four/five lines of five words
import string

# input_file = open("testFile.txt", 'r')
output_file = open("modTestFile.txt", 'w')

WORDS_PER_LINE = 5

word_count = 0

for line in input_file:
    line = line.strip()
    
    word = ''
    
    for char in line:
        if char not in string.whitespace + string.punctuation:
            word = word + char
        else:
            word_count = word_count + 1
            if word_count <= WORDS_PER_LINE:
                print(word, end=' ')
                print(word, end=' ', file=output_file)
            else:
                print()
                print(file=output_file)
                word_count = 0
            word = ''
                
input_file.close()
output_file.close()