trace = True

def typetest(**argchecks):
    return argumenttest(argchecks, lambda val, type: not isinstance(val, type))

def rangetest(**argchecks):
    return argumenttest(argchecks, lambda val, range: val < range[0] or val > range[1])

def argumenttest(argchecks, failCondition):
    def onDecorator(func):
        if not __debug__:
            return func
        else:
            code = func.__code__
            allArgsNames = list(code.co_varnames[:code.co_argcount])

            def onError(argname, criteria):
                errMsg = '%s argument "%s" is not %s'
                raise TypeError(errMsg % (func.__name__, argname, criteria))

            def onCall(*pargs, **kargs):
                positionalsArgsNames = allArgsNames[:len(pargs)]
                for (argname, criteria) in argchecks.items():
                    if argname in kargs:
                        if failCondition(kargs[argname], criteria):
                            onError(argname, criteria)

                    elif argname in positionalsArgsNames:
                        position = positionalsArgsNames.index(argname)
                        if failCondition(pargs[position], criteria):
                            onError(argname, criteria)
                    else:
                        if trace:
                            print('Argument "{0} defaulted'.format(argname))

                return func(*pargs, **kargs)
            return onCall
    return onDecorator

@typetest(a = int, c=float)
def func(a, b, c, d):
    print(a, b, c, d)

@rangetest(age = (0, 120))
def persinfo(name, age):
    print('%s is %s years old' % (name, age))

func(1, 2, 3.0, 4)
# func('spam', 2, 99, 4)

class C:
    @rangetest(a=(1, 10))
    def meth1(self, a):
        return a * 1000

    @typetest(a = int)
    def meth2(self, a):
        return a * 1000

X = C()
print(X.meth1(5))
# print(X.meth1(20))