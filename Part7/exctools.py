'''
Created on Sep 9, 2021

@author: osboxes
'''

def safe(func, *pargs, **kargs):
    try:
        func(*pargs, **kargs)
    except Exception:
        import sys
        print(sys.exc_info())
        import traceback
        traceback.print_exc()
        
if __name__ == "__main__":
    import oops
    safe(oops.oops)