# classify a range of numbers with respect to perfect, abundant or deficient
# unless otherwise stated, variables are assumed to be of type int. Rule 4

top_num_str = input("What is the upper number for the range:")
top_num = int(top_num_str)

for number in range(2, top_num+1):
    # sum the divisors of number
    sum_of_divisors = 0
    for divisor in range(1, number):
        if number % divisor == 0:
            sum_of_divisors = sum_of_divisors + divisor
    # classify the number based on its divisor sum
    if number == sum_of_divisors:
        print(number,"is perfect")
    elif number < sum_of_divisors:
        print(number,"is abundant")
    else:
        print(number,"is deficient")
