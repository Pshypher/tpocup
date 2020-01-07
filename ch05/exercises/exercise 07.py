# Program counts the frequency of each letter (a through z) from the words
# stored in a file words.txt that contains a paragraph of random words. Each
# letter and the value of its count in the words.txt file are stored in a
# dictionary
import string

freq_count_dict = {}
for alphabet in string.ascii_lowercase:
    freq_count_dict[alphabet] = 0

file_name = input("Enter file name: ")
while True:
    try:
        input_file = open(file_name, 'r')
        for line in input_file:
            for char in line:
                if char == 'a':
                    freq_count_dict['a'] += 1
                elif char == 'b':
                    freq_count_dict['b'] += 1
                elif char == 'c':
                    freq_count_dict['c'] += 1
                elif char == 'd':
                    freq_count_dict['d'] += 1
                elif char == 'e':
                    freq_count_dict['e'] += 1
                elif char == 'f':
                    freq_count_dict['f'] += 1
                elif char == 'g':
                    freq_count_dict['g'] += 1
                elif char == 'h':
                    freq_count_dict['h'] += 1
                elif char == 'i':
                    freq_count_dict['i'] += 1
                elif char == 'j':
                    freq_count_dict['j'] += 1
                elif char == 'k':
                    freq_count_dict['k'] += 1
                elif char == 'l':
                    freq_count_dict['l'] += 1
                elif char == 'm':
                    freq_count_dict['m'] += 1
                elif char == 'n':
                    freq_count_dict['n'] += 1
                elif char == 'o':
                    freq_count_dict['o'] += 1
                elif char == 'p':
                    freq_count_dict['p'] += 1
                elif char == 'q':
                    freq_count_dict['q'] += 1
                elif char == 'r':
                    freq_count_dict['r'] += 1
                elif char == 's':
                    freq_count_dict['s'] += 1
                elif char == 't':
                    freq_count_dict['t'] += 1
                elif char == 'u':
                    freq_count_dict['u'] += 1
                elif char == 'v':
                    freq_count_dict['v'] += 1
                elif char == 'w':
                    freq_count_dict['w'] += 1
                elif char == 'x':
                    freq_count_dict['x'] += 1
                elif char == 'y':
                    freq_count_dict['y'] += 1
                elif char == 'z':
                    freq_count_dict['z'] += 1
                else:
                    continue
        input_file.close()
        break
    except FileNotFoundError:
        print('File "', file_name, '"does not exist.')
        file_name = input("Enter file name: ")

for key in freq_count_dict:
    print("{0:<2s}:{1:>4d}".format(key, freq_count_dict[key]))