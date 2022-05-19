traceMe = False
def trace(*args):
    if traceMe: print('[' + ' '.join(map(str, args)) + ']')

class BuiltinsMixin:
    def __str__(self):
        return self.__class__.__getattr__(self, '__str__')()

def Private(*privates):
    def onDecorator(aClass):
        if not __debug__:
            return aClass

        class onInstance(BuiltinsMixin):
            def __init__(self, *args, **kargs):
                self.wrapped = aClass(*args, **kargs)
            
            def __getattr__(self, attr):
                trace('get:', attr)
                if attr in privates:
                    raise TypeError('private attribute fetch: ' + attr)
                else:
                    return getattr(self.wrapped, attr)

            def __setattr__(self, attr, value):
                trace('set:', attr)
                if attr == 'wrapped':
                    print('__dict__')
                    self.__dict__[attr] = value
                elif attr in privates:
                    raise TypeError('private attribute fetch: ' + attr)
                else:
                    print('setattr')
                    setattr(self.wrapped, attr, value)

        return onInstance
    return onDecorator

if __name__ == '__main__':
    traceMe = True

    @Private('data', 'size')
    class Doubler:
        def __init__(self, label, start):
            self.label = label
            self.data = start
        def size(self):
            return len(self.data)
        def double(self):
            for i in range(self.size()):
                self.data[i] = self.data[i] * 2
        def display(self):
            print('%s => %s' % (self.label, self.data))

    # X = Doubler('X is', [1, 2, 3])
    # Y = Doubler('Y is', [-10, -20, -30])
    
    # Following will succeed
    # print(X.label)
    # X.display()
    # print(Y.label)
    # Y.display()

    # Following will fail
    # print(X.size())

    @Private('age')
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
        def __str__(self):
            return 'Person: ' + str(self.age)
        def __add__(self, yrs):
            self.age += yrs

    P = Person('Bob', 42)
    print('p')
    # P.age
    print(P)
    # P + 10
    # print(P)