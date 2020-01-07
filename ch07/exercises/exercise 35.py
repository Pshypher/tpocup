# Unless stated otherwise, variables are assumed to be of the str data type

def reverse_string(S):
    """Return the string S in reverse order using a for loop."""
    S_reverse = ""
    for ch in S:
        S_reverse = ch + S_reverse

    return S_reverse

# Prompt user for a string
chars = input("Enter a sequence of alphanumeric chars: ")
print(reverse_string(chars))
