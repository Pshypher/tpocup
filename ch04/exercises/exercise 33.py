# Changes the case of a string provided by the user to lowercase
# without calling the str.lower() method

UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWER = "abcdefghijklmnopqrstuvwxyz"

seq_str = input("Enter a string: ")
seq_all_lowercase = seq_str

for index, char in enumerate(UPPER):
    if char in seq_all_lowercase:
        seq_all_lowercase = seq_all_lowercase.replace(char, LOWER[index])

print("Original Sequence: {}\nLowercase Sequence: {}".format(seq_str, seq_all_lowercase)) 
