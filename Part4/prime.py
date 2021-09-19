'''
Measure performance with buildin timeit
import timeit
timeit.repeat(setup='from prime import prime', stmt='prime(16)', number=2, repeat=5)

With homegrown timer
import timer
timer.total(1000, prime.prime1, 1000)[0]

Results:
prime1.min = 7.3999999585794285e-06
prime.min = 5.074999990029028e-06

Other examples:
min(timeit.repeat(setup='from prime import prime,prime1', stmt='[(prime(16)),(prime1(16))]', number=2, repeat=3))
'''

def prime(y):
    if y < 4:
        print(y, "is not prime")
        return

    if y == 4:
        print(y, "has factor 2")
        return
    
    start = int(y//2)
    primes = [x for x in range(start,2,-1) if y%x == 0]
    if primes:
        print(y, "has factor ", primes)
    else:
        print(y, "is not prime")

def prime1(y):
    sign = -1 if y<0 else 1
    orig = y
    y = abs(y)
    
    if (y < 2):
        print(orig, 'is not prime')
        return
        
    x = y//2
    
    while x > 1:
        if y % x == 0:
            print(orig, 'has factor', x*sign)
            break
        x -= 1
    else:
        print(orig, 'is prime')


prime(0)
prime(1)
prime(2)
prime(3)
prime(4)
prime(5)
prime(6)
prime(13.0)
prime(15)
prime(15.0)

prime1(0)
prime1(1)
prime1(2)
prime1(3)
prime1(4)
prime1(5)
prime1(6)
prime1(13.0)
prime1(15)
prime1(15.0)

# prime(3)
# prime(-3)
# prime(-3.0)
# prime(-8)
# prime(-8.0)
# prime(0)
# prime(1)