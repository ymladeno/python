class tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func
    def __call__(self, *args, **kargs):
        print(self, *args, **kargs)
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        return self.func(*args, **kargs)
    # def __get__(self, instance, owner):
    #     return wrapper(self, instance)
    def __get__(self, instance, owner):
        def wrapper(*args, **kargs):
            return self(instance, *args, **kargs)
        return wrapper

# class wrapper:
#     def __init__(self, desc, subj):
#         self.desc = desc
#         self.subj = subj
#     def __call__(self, *args, **kargs):
#         return self.desc(self.subj, *args, **kargs)
        
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