# Program written to create a new list from an old list having the same number of
# elements, the elements of the new list are the sum of the element itself and its
# neighbors in the original list
# Unless stated otherwise, variables are assumed to be of the type int

listA = [10,20,30,40,50]
 
# initializes the listB as an empty list
listB = []

listB.append(listA[0]+listA[1]) # add 1st int of the original list to the 2nd
                                # int in the list,append result to listB
# for each item in original list from 1 to n-2
for i in range(1,len(listA)-1):
    # find the sum of the each the item itself along with the
    # items to the left and right of the current item
    sum_of_neighbors = sum(listA[i-1:i+2])
    listB.append(sum_of_neighbors)  # append the sum to the new list

listB.append(listA[len(listA)-2]+listA[-1]) # find the sum of the 2nd to the last integer and 
                                            # the last integer in listA and append to listB
print(listB)
