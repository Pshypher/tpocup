# classify a range of numbers with respect to perfect, abundant or deficient
# unless otherwise stated, variables are assumed to be of type int. Rule 4

top_num_str = input("What is the upper number for the range:")
top_num = int(top_num_str)
number = 2
abundant_num_count = 0
deficient_num_count = 0

while number <= top_num:
    # sum the divisors of number
    divisor = 1
    sum_of_divisors = 0
    while divisor <= number//2:
        if number % divisor == 0:
            sum_of_divisors = sum_of_divisors + divisor
        divisor = divisor + 1
    # classify the number based on its divisor sum
    if number == sum_of_divisors:
        print(number,"is perfect")
    elif number < sum_of_divisors:
        abundant_num_count += 1 
    else:
        deficient_num_count += 1
    number += 1
