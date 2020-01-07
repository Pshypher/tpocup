# Program creates a list of 20 even numbers without using an if statement.
# Unless stated otherwise, variables are assumed to be of type int

# initialize an empty list to keep the even numbers
even_integers_lst = []

# for each number x from 0 up to but not including the number 20
for x in range(20):
    # add the number x*2 to the list
    even_integers_lst.append(x*2)
# display the list of even integers
print("Even integers:", even_integers_lst)