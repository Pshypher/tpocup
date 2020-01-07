# Computes the gravitational force(F) and the acceleration due to gravity(g)
# where r is the radius of the earth, m1 the mass of the Earth
# r the radius of the Earth, m2 the mass upon which the gravitational force
# is exerted upon and the gravitational constant is G

r = 6378e3
m1 = 5.9742e24
G = 6.67300e-11
X = input("How many kg does Mr. Jones weigh? ")
m2 = int(X)

F = (G*m1*m2)/r**2
g = F/m2

print("The gravitational force(F) exerted on Mr. Jones with a mass of {}kg is {:.4f} \
and acceleration due to gravity(g) is {:.1f}".format(m2, F, g))

