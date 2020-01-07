# Program creates a new list of numbers such that the numbers at opposite
# ends of the list are added and appended to another list that starts out empty

# list_of_ints = [1,2,3,4,5,6,7,8,9]      # odd
list_of_ints = [0,1,2,3,4,5,6,7,8,9]  # even
 
combined_list = []  # List formed by summing up the first and last numbers,
                    # storing the result of the sum and repeating a similar
                    # sequence of operation for the second and second-to-last
                    # element and so on, traversing through until the middle 
                    # of the original list
j = -1      # Index from the end of the list
for i in range(len(list_of_ints)//2):
    combined_list.append(list_of_ints[i]+list_of_ints[j])
    j = j-1
else:
    if len(list_of_ints)%2:
        combined_list.append(list_of_ints[i+1])
    
print(combined_list)    # [10,10,10,10,5] if list_of_ints=[1,2,3,4,5,6,7,8,9]
                        # [9,9,9,9,9] if list_of_ints=[0,1,2,3,4,5,6,7,8,9]
