'''
Created on Aug 23, 2021

@author: osboxes
'''

from lister import Lister

class ListerSub(Lister):
    def __str__(self):
        bases = (base.__name__ for base in self.__class__.__bases__)
        return '<Instance of %s(%s), address %s:\n>' % (
                           self.__class__.__name__,
                           ','.join(bases),                 # My class's name
                           id(self))                        # My address
    
if __name__ == '__main__':
    import testmixin
    testmixin.tester(ListerSub)