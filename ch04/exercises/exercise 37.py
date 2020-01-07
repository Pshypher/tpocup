# Program compares two strings and prints the smaller of both strings

string_seq = input("Enter a string of characters: ")
another_str = input("Enter another string: ")
"""
if len(string_seq) > len(another_str):
    if another_str == string_seq[:len(another_str)]:
        smaller = another_str
    else:
        pass
elif len(string_seq) < len(another_str):
    if another_str[:len(string_seq)] == string_seq:
        smaller = string_seq
    else:
        pass
else:
    if another_str == string_seq:
        smaller = another_str
"""

if len(string_seq) < len(another_str):
    shorter_str = string_seq
else:
    shorter_str = another_str

for i in range(len(shorter_str)):
    if string_seq < another_str:
        print(string_seq, "is the smaller of both strings.")
        break
    elif another_str < string_seq:
        print(another_str, "is the smaller of both strings.")
        break
else:
    print("{} and {} are similar strings.".format(string_seq, another_str))


