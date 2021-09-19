'''
Created on Aug 15, 2021

@author: osboxes
'''

class Attrs:
    def __getattr__(self,name):
        print('Get attr %s' % name)

    def __setattr__(self,name,value):
        print('Set %s = %s' % (name,value))
