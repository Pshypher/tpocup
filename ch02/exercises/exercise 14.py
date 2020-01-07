# 1 * 8 + 1 = 9
# 12 * 8 + 2 = 98
# 123 * 8 + 3 = 987
# 1234 * 8 + 4 = 9876
# 12345 * 8 + 5 = 98765
# 123456 * 8 + 6 = 987654
# 1234567 * 8 + 7 = 9876543
# 12345678 * 8 + 8 = 98765432
# 123456789 * 8 + 9 = 987654321

num = 1
result = num * 8 + num
print(num, "*", 8, "+", num, "=", result)

for digit in range(2, 10):
    num = num * 10 + digit
    result = num * 8 + digit
    print(num, "*", 8, "+", digit, "=", result)
    
print()
    
# 1 * 9 + 2 = 11
# 12 * 9 + 3 = 111
# 123 * 9 + 4 = 1111
# 1234 * 9 + 5 = 11111
# 12345 * 9 + 6 = 111111
# 123456 * 9 + 7 = 1111111
# 1234567 * 9 + 8 = 11111111
# 12345678 * 9 + 9 = 111111111
# 123456789 * 9 + 10 = 1111111111

num = 1
result = num * 9 + (num+1) 
print(num, "*", 9, "+", num+1, "=", result)

for digit in range(2, 10):
    num = num * 10 + digit
    result = num * 9 + (digit+1)
    print(num, "*", 9, "+", digit+1, "=", result)
    
print()

# 9 * 9 + 7 = 88
# 98 * 9 + 6 = 888
# 987 * 9 + 5 = 8888
# 9876 * 9 + 4 = 88888
# 98765 * 9 + 3 = 888888
# 987654 * 9 + 2 = 8888888
# 9876543 * 9 + 1 = 88888888
# 98765432 * 9 + 0 = 888888888 

num = 9
delta = 2
result = num * 9 + (num-delta) 
print(num, "*", 9, "+", num-delta, "=", result)

for digit in range(8, 1, -1):
    delta = delta + 1
    num = num * 10 + digit
    result = num * 9 + (9-delta)
    print(num, "*", 9, "+", 9-delta, "=", result)
    
print

# 1 * 1 = 1
# 11 * 11 = 121
# 111 * 111 = 12321
# 1111 * 1111 = 1234321
# 11111 * 11111 = 123454321
# 111111 * 111111 = 12345654321
# 1111111 * 1111111 = 1234567654321
# 11111111 * 11111111 = 123456787654321
# 111111111 * 111111111 = 12345678987654321

num = 1
result = num * num
print(num, "*", num, "=", result)

for i in range(1, 9):
    num = num * 10 + 1
    result = num * num
    print(num, "*", num, "=", result)