
A,B,C,D = 0,0,0,0

while A <= 10:
    A += 2
    if A%3 == 0:
        B += 1
    else:
        C += 1
    D += 1

print( "A =", A )  # Line 1     A = 12
print( "B =", B )  # Line 2     B = 2
print( "C =", C )  # Line 3     C = 4
print( "D =", D )  # Line 4     D = 6

