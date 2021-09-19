"""
Compare sqrt variants
"""

import math, sys, timer                         # Import timer functions
reps = 10000
repslist = list(range(reps))                     # Hoist out, list in both 2.X/3.X

#...
# expected winner
def useSqrt():
    return list(map(math.sqrt, repslist))

def usePow():
    return list(map(lambda x: math.pow(x,.5), repslist))

def useExpr():
    return [x**.5 for x in repslist]

#...

print(sys.version)
for test in (useSqrt, usePow, useExpr):
    (bestof, (total, result)) = timer.bestoftotal(5, 1000, test)
    print ('%-9s: %.5f => [%s...%s]' %
           (test.__name__, bestof, result[0], result[-1]))
    
'''
Interactevely comparing dict comprehension and for loop
>>> min(timeit.repeat(stmt='res={}\nfor x in range(100): res[x]=x**2', number=100, repeat=10000))
0.0015363509992312174
>>> min(timeit.repeat(stmt='{x:x**2 for x in range(100)}', number=100, repeat=10000))
0.0014979780007706722
'''