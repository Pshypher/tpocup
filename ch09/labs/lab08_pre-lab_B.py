
M = {}
M[ "Joyce" ] = 7
M[ "Mike" ] = 12
M[ "Bea" ] = 9 

print( "M:", M )    # M: {"Joyce": 7, "Mike": 12, "Bea":9} 

if "Bea" in M:
    A = M[ "Bea" ]  
    print( "A:", A )# A: 9 
    
if "Joyce" in M:
    del M[ "Joyce" ]

print( "M:", M )    # M: {"Mike": 12, "Bea": 9}