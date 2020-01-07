# Telephone directory has P pages, N lines per page and
# C columns per line. The entire telephone directory has a total
# of E entries.

# Assume that page, line, column numbers and X all start from 1
C_str = input("Enter the number of column on a line: ")
X_str = input("What entry contains the name and number of individual? ")

C = int(C_str)
X = int(X_str)

column = X % C  # skip Entries evenly divisible C
line = X // C + 1
page = X // (column * line)     # A ZeroDivisionError when X % C is 0

print("Entry", X, "is on page", page, "line", line, "and column", column, ".")
