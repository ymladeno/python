'''
    Works on python3 and python2
'''
def tracer(func):
    def wrapper(*args, **kargs):
        wrapper.calls += 1
        print('call %s to %s' % (wrapper.calls, func.__name__))
        return func(*args, **kargs)
    wrapper.calls = 0
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