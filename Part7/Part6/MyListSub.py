'''
Created on Aug 9, 2021

@author: osboxes
'''

from MyList import MyList as MineList
from mylist import MyList as bookList

class MyListSub(MineList):
    countAdd = 0
    
    def __init(self, start = []):
        self.data = list(start)

    def __add__(self, y):
        print('Add ', y)
        MyListSub.countAdd += 1
        return MyListSub(getattr(self.data, '__add__')(y))

    @classmethod
    def getCount(cls):
        return cls.countAdd

class MyListSub1(bookList):
    countAdd = 0
    
    def __add__(self, y):
        print('Add ', y)
        MyListSub1.countAdd += 1
        return MyListSub1(bookList.__add__(self, y))

    @classmethod
    def getCount(cls):
        return cls.countAdd

def test1():
    print('******** Test 1 **********')
    l = MyListSub()
    l += [1,2,3]
    print(type(l), ': ', l)
    print('Counter: ', l.getCount(),'\n')

    l += [4,5]
    print(type(l), ': ', l)
    print('Counter: ', l.getCount(),'\n')

def test2():
    print('******** Test 2 **********')
    l = MyListSub1([0])
    l += [1,2,3]
    print(type(l), ': ', l)
    print('Counter: ', l.getCount(),'\n')

    l += [4,5]
    print(type(l), ': ', l)
    print('Counter: ', l.getCount(),'\n')

if __name__ == '__main__':
    test1()
    test2()