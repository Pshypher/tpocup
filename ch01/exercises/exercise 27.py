X_str = input("Enter the length of the first parallel side: ")
Y_str = input("Enter the length of the second parallel side: ")
H_str = input("Enter the height of the trapezoid: ")

X_int = int(X_str)
Y_int = int(Y_str)
H_int = int(H_str)

area = (X_int + Y_int) / 2 * H_int

print("The area of the trapezoid of sides {2} and {1} meters and height {0} meter \
is {3} meter square.".format(H_int,Y_int,X_int,area)) 
