# Palindrome tester
import string

original_str = input('Input a string: ')
modified_str = original_str.lower()
alphanumeric_str = ''

good_chars = string.ascii_lowercase

for char in modified_str:
    if char in good_chars:   # keep good characters only
        alphanumeric_str = alphanumeric_str + char

if alphanumeric_str == alphanumeric_str[::-1]:  # it is a palindrome
    print(\
'The original string is: {}\n\
the modified string is: {}\n\
the reversal is:        {}\n\
String is a palindrome'.format(original_str, alphanumeric_str, alphanumeric_str[::-1]))
else:
    print(\
'The original string is: {}\n\
the modified string is: {}\n\
the reversal is:        {}\n\
String is not a palindrome'.format(original_str, alphanumeric_str, alphanumeric_str[::-1]))
