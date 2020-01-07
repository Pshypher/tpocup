
A = 3 * [25]
print( "A:", A )           

B = 3 * list( "25" )
print( "B:", B )            

C = "a" in ["aardvark"]
print( "C:", C )            

D = "a" in ["a","n","t"]
print( "D:", D )            

E = ["Arthur", "King", "of", "the", "Britons"]
print("E:", E)

print("E[1]:", E[1])
print("E[1][2]:", E[1][2])
print("E[:2]:", E[:2])

F = []
F.append( 45 )
for n in range(4):
    F.append( 10*n-3 )

print( "F:", F )            

G = [ 10, 20, 30, 40, 20 ]
H = G.pop()
print("H:",H,", G:",G)

G = [ 10, 20, 30, 40, 20 ]
print("G:", G)
I = G.index( 40 )
J = G.count( 20 )
print( "I:",I, ", J:", J )

K = [ 15, -7, 12, -4, 14 ]
print("K:",K)
print("sorted(K):", sorted(K))
print("K:",K)
K.sort()
print("K:",K)


L = " to be, or not to be "
print("L:",L)
M = L.split()
print( "M:", M )            
N = L.split( "," )
print( "N:", N )            

P = [ "One", "Two", "Three" ]
print("P:", P)
Q = " ".join( P )
print( "Q:", Q )            

R = ", ".join( P )
print( "R:", R )           

S = "Hello World"
print("S:", S)
T = S.split()
print("T:", T)

for item in T:
    print(item)
print("----------")   
for a,b in enumerate(T):
    print(a,b)

    
