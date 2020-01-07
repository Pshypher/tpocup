import math

# Calculate the angle of a triangle given the length
# of all the sides using the cosine rule
a = 3
b = 7
c = 9
C = math.degrees(math.acos((c**2 - (a**2 + b**2))/(-2*a*b)))
B = math.degrees(math.acos((b**2 - (c**2 + a**2))/(-2*a*c)))
A = math.degrees(math.acos((a**2 - (b**2 + c**2))/(-2*b*c)))

print("< BAC is", round(A), "< ABC is", round(B), "and < BCA", round(C))

