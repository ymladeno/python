trace = True

def rangetest(**argchecks):
    def onDecorator(func):
        if not __debug__:
            return func
        else:
            code = func.__code__
            allargs = code.co_varnames[:code.co_argcount]
            funcname = func.__name__
            def onCall(*pargs, **kargs):
                expected = list(allargs)
                positionals = expected[:len(pargs)]

                for (argname, (low, high)) in argchecks.items():
                    if argname in kargs:
                        if kargs[argname] < low or kargs[argname] > high:
                            errmsg = '{0} argument "{1}" not in {2}..{3}'
                            errmsg = errmsg.format(funcname, argname, low, high)
                            raise TypeError(errmsg)
                    elif argname in positionals:
                        position = positionals.index(argname)
                        if pargs[position] < low or pargs[position] > high:
                            errmsg = '{0} argument "{1}" not in {2}..{3}'
                            errmsg = errmsg.format(funcname, argname, low, high)
                            raise TypeError(errmsg)
                    else:
                        if trace:
                            print('Argument "{0} defaulted'.format(argname))
                return func(*pargs, **kargs)
            return onCall
    return onDecorator

@rangetest(age = (0, 120))
def persinfo(name, age):
    print('%s is %s years old' % (name, age))

class Person:
    def __init__(self, name, job, pay):
        self.job = job
        self.pay = pay

    @rangetest(percent = (0.0, 1.0))
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

persinfo('Bob Smith', 45)

sue = Person('Sue Jones', 'dev', 100000)
sue.giveRaise(.10)
print(sue.pay)