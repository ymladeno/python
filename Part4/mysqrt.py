from math import sqrt

L=[2,4,9,16,25]

FOR=[]
for x in L:
    FOR.append(sqrt(x))
    
MAP=list(map(sqrt, L))

LIST=[sqrt(x) for x in L]
GEN=list(sqrt(x) for x in L)

print(FOR, MAP, LIST, GEN, sep='\n')