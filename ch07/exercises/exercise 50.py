# Program written to transfer the elements of a list to another
# list whilst rearranging the order in which the elements appear

# Unless stated otherwise, variables are assumed to be of type int

def transform(list1, list2, r1, r2):
    """Removes items from list1 in the slice r1:r2, appends them onto list2
        in reverse order; Returns the resulting list."""
    slice_lst = list1[r1:r2]    # r1 < r2
    slice_lst.reverse()         # reverse the order of the slice
    list2.extend(slice_lst)     # add the elements sliced from list1 
                                # now reversed to list2
    return list2

# Test that the function above works as expected
list1 = [1,2,3,4,5,6,7,8,9]
list2 = [100,200]
transform(list1, list2, 4, 7)
print(list2)        # displays [100,200,7,6,5]

