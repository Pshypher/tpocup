operators = ['+', '']

# Using the addition operator succesive digits are summed to see which
# combination of numbers and the addition operator sums up to 99

for a in operators:
    for b in operators:
        for c in operators:      
            for d in operators:
                for e in operators:
                    for f in operators:
                        for g in operators:
                            for h in operators:
                                expression = '1{}2{}3{}4{}5{}6{}7{}8{}9'.format(
                                    a,b,c,d,e,f,g,h)
                                if eval(expression)==99:
                                    print(expression)
                                                                                
operators = ['+','-','*','/','']
count = 0

# Using all standard four operators +,-,*,and/ against the successive digits
# 123456789, the number of times their operations yield the number 99 is 
# counted and displayed
for a in operators:
    for b in operators:
        for c in operators:      
            for d in operators:
                for e in operators:
                    for f in operators:
                        for g in operators:
                            for h in operators:
                                expression = '1{}2{}3{}4{}5{}6{}7{}8{}9'.format(
                                    a,b,c,d,e,f,g,h)
                                if eval(expression)==99:
                                    count += 1

print()
print("Using (+-*/) 1 2 3 4 5 6 7 8 9==99",count,"times")