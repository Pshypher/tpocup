# Program designed to read in a paragraph from a file, scramble the internal
# letters of each word, and then write the result to a file

# Create a file handler object for the file so named "excerpt.txt" to be read.
# Another file descriptor object named "scrambled_text.txt".
# Iterate through the lines of the paragraph.
    # For each word contained in each line of the paragraph of text
            # words are seperated by whitespace characters.
        # The variables first_char and last_char hold the first and last_char
        # of each word.
        # Slice the internal letters of each word excluding the first and last
        # character and assign to the variable chars_within_str.
        # Using ROT 13, for each character in the variable chars_within_str
            # Rotate the character 13 characters after its own
            # Replace the character in place with the character from the
            # ROT 13 operation.
        # Concatenate first_char and last_char to the beginning and end
        # of chars_within_str variable respectively.
        # Concatenate the result of each scrambled word to out_line
    # Write the content of the string out_line to the file descriptor for the
    # file named "scrambled_words.txt"
# Close both the input and output file descriptors.

import string

ROT = 13
ALPHABETS = 26

input_file = open("excerpt.txt", 'r')
output_file = open("scrambled_text01.txt", 'w')



for line in input_file:
    
    out_line = ""

    while line != '':
        
        # A try-except block is used to catch the ValueError returned by the
        # string object .index() method which is used to search for space
        # characters that delimit each word and also the last character that is 
        # not succeeded by a space character.
        try:
            end = line.index(" ")
        except ValueError:
            end = len(line)
            
        word = line[:end]
        
        for i in range(len(word)-1, 0, -1):
            if word[i] not in string.punctuation + string.whitespace:
                final_chars_index = i
                final_chars = word[i:]
                break
    
        chars_within_str = word[1:final_chars_index]

        for i, char in enumerate(chars_within_str):
            char = char.lower()
            if char not in string.ascii_lowercase:
                continue
            rot13_char = chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
            chars_within_str = chars_within_str[:i] + rot13_char + \
                chars_within_str[i+1:]
            
        word = word[0] + chars_within_str + final_chars
        final_chars = ''
        out_line = out_line + word + " "
        
        line = line[end+1:]

    out_line = out_line.strip()
    print(out_line, file=output_file)
    
input_file.close()
output_file.close()