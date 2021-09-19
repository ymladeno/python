'''
Created on Sep 9, 2021

@author: osboxes
'''

class MyError(Exception): pass

def oops():
    raise MyError('Spam')

def foo():
    try:
        oops()
    except MyError as myerror:
        print(MyError, myerror)
        # print(myerror.__class__)
        # import sys
        # print(sys.exc_info())
    except IndexError:
        print("indexError")

if __name__ == '__main__':
    foo()