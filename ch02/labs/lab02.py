# continue to process values until the user enters the value 0
# ignore all negative integers
# count the number of odd integers entered
# count the number of even integers entered
# calculate the sum of odd integers in the series
# calculate the sum of even integers in the series
# display the sum of odds
# display the sum of evens
# display the count of odds
# display the count of evens
# display the total number of positive integers entered

# unless otherwise stated, variables are of type int

n_str = input("Input an integer (0 terminates): ")
n = int(n_str)

odd_count = 0
even_count = 0
odd_sum = 0
even_sum = 0
positive_int_count = 0

while n != 0:
    if n < 0:
        print(n, "is a negative integer")
        n_str = input("Input an integer (0 terminates): ")
        n = int(n_str)
        continue
    if n%2:
        odd_sum = odd_sum + n
        odd_count = odd_count + 1
    else:
        even_sum = even_sum + n
        even_count = even_count + 1
    positive_int_count = positive_int_count + 1
    n_str = input("Input an integer (0 terminates): ")
    n = int(n_str)

# Good stuff goes here

print()
print("sum of odds:", odd_sum)
print("sum of evens:", even_sum)
print("odd count:", odd_count)
print("even count:", even_count)
print("total positive int count:", positive_int_count)
