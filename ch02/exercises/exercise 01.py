# displays numbers between 100 and 999 divisible by 17
for number in range(100, 1000):
    if number % 17:
        continue
    print(number, end=' ')
    
