# Program creates a list of 20 even numbers without using an if statement.
# Unless stated otherwise, variables are assumed to be of type int

even_integers_lst = [x*2 for x in range(20)]    # for each number x from 0 up to 19
                                                # add the number x*2 to the list
# display the list of even integers
print("Even integers:", even_integers_lst)
