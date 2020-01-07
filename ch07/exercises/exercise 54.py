# Program written to solve a puzzle in which the sum of a
# pair of numbers from 1-18 are perfect squares, Sally invites 17
# guest and keeps the number 1 for herself, the program finds the number
# assigned to Sally's partner

# Unless stated otherwise, assume variables are of the list data type

import math


def is_perfect_square(N):
    """Checks if the argument N is a perfect square. Returns a boolean
        True if N is a perfect square otherwise False."""
    
    root = int(math.sqrt(N))
    return root * root == N


def in_guest_lst(T, guests):
    """Checks if either or both of the couples paired together are already
        in the guest list guests: Return a bool value, True if either one of
        the guest is already in the list otherwise False."""
    already_paired = False
    
    for pair in guests:
        if T[0] in pair or T[1] in pair:
            already_paired = True
            
    return already_paired
    
    
# From 1-9 append a list of the combination of the perfect squares in the
# perfect_square_sum_pairs
# Size of the combination should be 9 (2 operands summed together)
# from a total of 18 numbers
perfect_square_sum_pairs = []
for i in range(1,10):
    for j in range(i+1,19):
        if is_perfect_square(i+j):  # determine if a  number is a perfect
                                    # square
            # A list of lists to hold the combinations for each pair of
            # numbers that sum up to a perfect square   
            if len(perfect_square_sum_pairs) < i:
                perfect_square_sum_pairs.append([])
            perfect_square_sum_pairs[i-1].append((i,j))


# Find all possible combinations of how each guest can be paired with 
# one another using the list of tuple pair that sum up to perfect squares
for a in perfect_square_sum_pairs[0]:
    for b in perfect_square_sum_pairs[1]:
        for c in perfect_square_sum_pairs[2]:
            for d in perfect_square_sum_pairs[3]:
                for g in perfect_square_sum_pairs[6]:
                    for e in perfect_square_sum_pairs[4]:
                        for f in perfect_square_sum_pairs[5]:
                            for h in perfect_square_sum_pairs[7]:
                                for i in perfect_square_sum_pairs[8]:
                                    guest_lst = []
                                    for j in [a,b,c,d,e,f,g,h,i]:
                                       if not in_guest_lst(j, guest_lst):
                                           guest_lst.append(j)
    if len(guest_lst)==9:
        break
    
# Display the guest no. of the guest Sally is paired with
print("Sally is paired with guest no.", guest_lst[0][1])