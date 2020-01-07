
A,B,C = 0,0,0

for N in range(11):
    if N%2 == 0:
        A += 1
    elif N%3 == 0:
        B += 1
    else:
        C += 1

print("A =", A)  # Line 1       A = 6
print("B =", B)  # Line 2       B = 2
print("C =", C)  # Line 3       C = 3
print("N =", N)  # Line 4       D = 10
