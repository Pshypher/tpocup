# Build different possible string combinations from a list of integers
# ['2', '3', '4', '5'] and a list of integer operations ['+','-','*','/','**']
# All expressions are displayed using all four numbers exactly once and three
# of the integer operators exactly once

# Unless stated otherwise, variables are assumed to be of the type str

int_operands_lst = ['2','3','4','5']
int_operators_lst = ['+','-','*','/','**']

found_bool = False

for i in int_operators_lst:
    for j in int_operators_lst:
        for k in int_operators_lst:
            for a in int_operands_lst:
                for b in int_operands_lst:
                    for c in int_operands_lst:
                        for d in int_operands_lst:
                            if (a!=b and a!=c and a!=d and b!=c and b!=d and
                                c!=d and i!=j and i!=k and j!=k):
                                expression_str = a+i+b+j+c+k+d
                                if eval(expression_str)==26:
                                    print(expression_str)
                                    found_bool = True
    if found_bool:
        break

                                 
                                