import time, sys

def timer(label = '', trace = True):
    class Timer:
        def __init__(self, func):
            self.func = func
            self.alltime = 0
        def __call__(self, *args, **kargs):
            start = time.clock()
            result = self.func(*args, **kargs)
            elapsed = time.clock() - start
            self.alltime += elapsed
            if trace:
                print('%s %s: %.5f, %.5f' % (label, self.func.__name__, elapsed, self.alltime))
            return result
        def __get__(self, instance, owner):
            def wrapper(*args, **kargs):
                return self(instance, *args, **kargs)
            return wrapper
    return Timer

@timer(label = '[CCC]==>')
def listcomp(N):
    return [x * 2 for x in range(N)]

@timer(label = '[MMM]==>')
def mapcall(N):
    return list(map(lambda x: x * 2, range(N)))

listcomp(10000)
print('allTime = %s' % listcomp.alltime)
print('')
mapcall(10000)
print('allTime = %s' % mapcall.alltime)

class Person:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    @timer(label = '**')
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)
    
    @timer(label = '**')
    def lastName(self):
        return self.name.split()[-1]

bob = Person('Bob Smith', 50000)
bob.giveRaise(.25)
print(bob.lastName())