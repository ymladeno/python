'''
Created on Aug 11, 2021

@author: osboxes
'''
from numpy.ma.extras import issequence
from copy import deepcopy

class Attrs:
    def __init__(self, x):
        if issequence(x):
            print('Make new sequence')
            self._x = deepcopy(x)
        else:
            self._x = x

    def __getattr__(self,name):
        if name == 'age':
            return 40
        else:
            return 0
            
    def getAttrs(self):
        print('Get value of x')
        return self._x

    def setAttrs(self, x):
        print('Set x = ', x)
        self._x = x

    def __repr__(self):
        return str(self._x)

    attr = property(getAttrs, setAttrs, None, None)

if __name__ == '__main__':
    a = Attrs(1)
    print('attr = ', a.attr)
    a.attr = 10
    print('attr = ', a.attr)
    print('Age: ', a.age)
    a.age = 50
    print('attr = ', a.age)
