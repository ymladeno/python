'''
    Works only in python3, because it uses keyword - nonlocal
'''
def tracer(func):
    calls = 0
    def wrapper(*args, **kargs):
        nonlocal calls
        calls += 1
        print('call %s to %s' % (calls, func.__name__))
        return func(*args, **kargs)
    return wrapper

@tracer
def spam(a,b,c):
    print(a + b + c)

@tracer
def eggs(x,y):
    print(x ** y)

spam(1,2,3)
spam(2,4,1)

eggs(2,16)

class Person:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    @tracer
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)
    
    @tracer
    def lastName(self):
        return self.name.split()[-1]

bob = Person('Bob Smith', 50000)
bob.giveRaise(.25)