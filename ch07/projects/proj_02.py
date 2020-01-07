def generate_pascals_triangle(height_int):
    """Generates the binomial coefficient for a certain exponent from x=1 to
        x=height_int. The arrangements of the binomial coefficients from 1 to
        height_int cascades to form what is called Pascal's triangle. Returns
        Pascal's triangle represented as a list of row lists."""
    triangle_list = []
    
    # For each row from 1 to the height of the triangle
    for i in range(1, height_int+1):
        coefficients_list = []  # An empty list where the coefficients for each
                                # row is kept
        # For each row in pascal's triangle [i] element(s) long
        for j in range(i):
            if not triangle_list:               # Begin by adding a single 
                coefficients_list.append(1)     # element 1 to the first row
                break
            # If the index isn't the first of last element for the row
            # sum up the 2 elements in the row directly above it i.e
            # the elements in the previous row above it
            if j>0 and j<i-1:
                coefficient_int = triangle_list[-1][j-1] + \
                                  triangle_list[-1][j]
                coefficients_list.append(coefficient_int)
            else:   # Otherwise add the element at edge of previous row to the
                coefficients_list.append(triangle_list[-1][-1]) # edge of the
                                                                # current row
        triangle_list.append(coefficients_list)
        
    return triangle_list

# Program designed to model Pascal's triangle, a user is prompted for the
# height of the triangle and the triangle is generated in the same style as
# shown below
#       1
#      1 1
#     1 2 1
#    1 3 3 1
#   1 4 6 4 1
# 1 5 10 10 5 1

# Prompt user for the height of the triangle
height_str = input("Enter the height of the triangle: ")
height_int = int(height_str)
triangle_list = generate_pascals_triangle(height_int)

# Display the triangle in a nicely outputted format 

# We find the width of the last element first converting each of its element
# to a string and joining all the elements together seperating each of them
# with a whitespace
base_row = [str(i) for i in triangle_list[-1]]  # int(i) -> str(i)
base_row_str = ' '.join(base_row)
width = len(base_row_str)

for row_list in triangle_list:
    row_list = [str(i) for i in row_list]   # Convert each element of the row
                                            # to a string
    row_str = ' '.join(row_list)
    # align each of the rows at the center with respect to that of the
    # last row in the triangle
    print('{0:^{1}s}'.format(row_str,width))    