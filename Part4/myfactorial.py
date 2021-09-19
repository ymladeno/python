from functools import reduce
from math import factorial
import timeit

def fact1(N):
    if (N == 0):
        return 1
    return N*fact1(N-1)

def fact2(N):
    return reduce(lambda x, y: x*y, range(N,0,-1))

def fact3(N):
    res=1
    for x in range(N,0,-1):
        res *= x
    return res

def fact4(N):
    return factorial(N)

# will print twice, because of setup
# for test in (fact1, fact2, fact3, fact4):
    # print('%-6s: %d => %.10f' % 
          # (test.__name__, test(6), min(timeit.repeat(setup='from myfactorial import test',stmt='test(6)', number=100, repeat=10000))))
    
'''
Use interactively:
>>> min(timeit.repeat(setup='from myfactorial import fact1', stmt='fact1(6)', number=100, repeat=10000))
4.28809998993529e-05
>>> min(timeit.repeat(setup='from myfactorial import fact2', stmt='fact2(6)', number=100, repeat=10000))
4.541199996310752e-05
>>> min(timeit.repeat(setup='from myfactorial import fact3', stmt='fact3(6)', number=100, repeat=10000))
2.9642998924828134e-05
>>> min(timeit.repeat(setup='from myfactorial import fact4', stmt='fact4(6)', number=100, repeat=10000))
6.729000233463012e-06

builtin math.factorial is fastest
'''