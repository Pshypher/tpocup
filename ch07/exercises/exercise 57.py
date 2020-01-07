# Program solves the puzzle posed by Jim Loy (http://www.jimloy.com) that
# involves three numeric palindromes.The first is two digits long, the second
# is three digits long, and when those two numbers are added together, we get
# the third number, which is four digits long. The program is written
# to find those three numbers.

def is_palindrome(S):
    """Checks if the string argument S is a palindrome: Return True if S
        is a palindrome otherwise False."""
    
    while len(S)>1:
        if S[0] != S[-1]:
            palindrome = False
            break
        S = S[1:-1]
    else:
        palindrome = True
        
    return palindrome
        

for x in range(100):    # For each two digit integer 00-99
    for y in range(1000):   # For each three digit integer 000-999
        x_str = "{:02d}".format(x)
        y_str = "{:03d}".format(y)
        # x and y are both palindrome
        if is_palindrome(x_str) and is_palindrome(y_str):
            # check that x+y is a four digit integer and x+y
            # is also a palindrome
            if len(str(x+y))==4 and is_palindrome(str(x+y)):
                numbers_lst = [x,y,x+y]
                
print(numbers_lst[0],'+',numbers_lst[1],'=',numbers_lst[2])
    

