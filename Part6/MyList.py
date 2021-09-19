'''
Created on Aug 8, 2021

@author: osboxes
'''

class MyList:
    def __init__(self, start=[]):
        self.data = start[:]

    def __add__(self, y):
        print('Add ', y)
        if isinstance(y, list):
            for x in y:  self.data.append(x) 
        else: self.data.append(y)

    def __radd__(self, y):
        print('radd ', y)
        tmp = self.data[:]
        self.data = y[:]
        y = tmp
        self.__add__(y)

    def __getitem__(self,i):
        print('Get from index ', i)
        return self.data[i]

    def __iter__(self):
        print(self.__iter__.__name__)
        return self.data.__iter__()

    def __repr__(self):
        return str(self.data)

    def append(self, y):
        print('Append ', y)
        self.__add__(y)
    
    def sort(self):
        print('Sorted') 
        self.data.sort()
