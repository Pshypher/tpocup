# Converts the inputted string into all lowercase alphabets
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower = 'abcdefghijklmnopqrstuvwxyz'

sequence_str = input("Enter a string of characters: ")

for index in range(len(upper)):
    if upper[index] in sequence_str:
        sequence_str = sequence_str.replace(upper[index], lower[index])

print(sequence_str)
