# Progam creates the lowercase English alphabet sequence from two substring 
# sequence variables 'x' and 'y' and displays the result
x = 'acegikmoqsuwy'
y = '+bdfhjlnprtvxz'
z = ''

for index in range(len(x)):
    z = z + x[index] + y[index+1]

for char in z:
    print(char, end=' ')
