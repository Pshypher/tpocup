M = { 200: "EE", 100: "ME", 500: "CPS" }

A = 100 in M
print( "A:", A )              # A: True

B = "ME" in M
print( "B:", B )              # B: False


print( "M[100]:", M[100] )    # M[100]: ME

M[500] = "CS"
print( "M[500]:", M[500] )    # M[500]: CPS

print( "M.keys():" )          # M.keys(): 200, 100, 500
for key in M.keys():          
    print( key )              
                              
print( "M.values():" )        # M.values(): EE, ME, CPS 
for value in M.values():      
    print( value )            
                              
print( "M.items():" )         # M.items(): 
for key, value in M.items():    # 200 EE
    print( key, value )         # 100 ME
                                # 500 CPS
print( "M:" )                 # M: 200, 100, 500
for X in M:
    print( X )
