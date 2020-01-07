# Converts a string that is all capitals into a string where only the
# first letters of each word delimited by space characters are capitals
# i.e. "NEW YORK" to "New York"

upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower = 'abcdefghijklmnopqrstuvwxyz'

sequence_str = input("Enter a string of characters: ")
cap_str = "" + sequence_str[0]

for index in range(1, len(sequence_str)):
    if (sequence_str[index-1] == ' ') or \
       not (sequence_str[index] in upper):
        cap_str = cap_str + sequence_str[index]
        continue
    cap_str = cap_str + lower[upper.find(sequence_str[index])]

print(cap_str)

