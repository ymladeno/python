def rangetest(*argchecks):
    def onDecorator(func):
        if not __debug__:
            return func
        else:
            def onCall(*args):
                for (ix, low, high) in argchecks:
                    if args[ix] < low or args[ix] > high:
                        errmsg = 'Arguments &s not in %s..%s' % (ix, low, high)
                        raise TypeError(errmsg)
                return func(*args)
            return onCall
    return onDecorator

@rangetest((1, 0, 120))
def persinfo(name, age):
    print('%s is %s years old' % (name, age))

class Person:
    def __init__(self, name, job, pay):
        self.job = job
        self.pay = pay

    @rangetest([1, 0.0, 1.0])
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

persinfo('Bob Smith', 45)
sue = Person('Sue Jones', 'dev', 100000)
sue.giveRaise(.10)
print(sue.pay)