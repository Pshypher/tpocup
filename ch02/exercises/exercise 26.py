#   SEND
# + MORE
# ------
#  MONEY



D = 0
while D <= 9:
    E = 0
    while E <= 9:
        M = 1
        while M <= 9:
            N = 0
            while N <= 9:
                O = 0
                while O <= 9:
                    R = 0
                    while R <= 9:
                        S = 1
                        while S <= 9:
                            Y = 0
                            while Y <= 9:
                                if (S*1000 + E*100 + N*10 + D) + (M*1000 + O*100 + R*10 + E) == (M*10000 + O*1000 + N*100+ E*10 + Y) \
                                   and D != E and D != M and D != N and D != O and D != R and D != S and D != Y \
                                   and E != M and E != N and E != O and E != R and E != S and E != Y \
                                   and M != N and M != O and M != R and M != S and M != Y \
                                   and N != O and N != R and N != S and N != Y \
                                   and O != R and O != S and O != Y \
                                   and R != S and R != Y \
                                   and S != Y:
                                    print("SOLUTION DEMNORSY:",D,E,M,N,O,R,S,Y)
                                    D,E,M,N,O,R,S,Y = 10,10,10,10,10,10,10,10
                                Y += 1
                            S += 1
                        R += 1
                    O += 1
                N += 1
            M += 1
        E += 1
    D += 1
    

