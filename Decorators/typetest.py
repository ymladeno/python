trace = True

def typetest(**argchecks):
    def onDecorator(func):
        if not __debug__:
            return func
        else:
            code = func.__code__
            allargs = code.co_varnames[:code.co_argcount]
            funcname = func.__name__
            print(f'args: {allargs}')
            print(f'args1: {argchecks}')

            def onCall(*pargs, **kargs):
                positionals = list(allargs)[:len(pargs)]
                print(f'pos names: {positionals}')
                print(f'pos1 vals: {pargs}')
                print(f'kargs: {kargs}')

                for (argname, type) in argchecks.items():
                    if argname in kargs:
                        if not isinstance(kargs[argname], type):
                            errmsg = '{0} argument "{1}" is not type {2}'
                            errmsg = errmsg.format(funcname, argname, type)
                            raise TypeError(errmsg)
                    elif argname in positionals:
                        position = positionals.index(argname)
                        if not isinstance(pargs[position], type):
                            errmsg = '{0} argument "{1}" is not type {2}'
                            errmsg = errmsg.format(funcname, argname, type)
                            raise TypeError(errmsg)
                    else:
                        if trace:
                            print('Argument "{0} defaulted'.format(argname))
                return func(*pargs, **kargs)
            return onCall
    return onDecorator

@typetest(a = int, c=float)
def func(a, b, c, d):
    print(a, b, c, d)

func(1, 2, 3.0, 4)
# func('spam', 2, 99, 4)