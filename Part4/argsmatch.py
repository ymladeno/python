def f1(a,b): print(a,b)         #positional arguments
def f2(a,*b): print(a,b)
def f3(a,**b): print(a,b)
def f4(a,*b,**c): print(a,b,c)
def f5(a,b=2,c=3): print(a,b,c)
def f6(a,b=2,*c): print(a,b,c)

#f1(1,2) caller uses positinal arguments
#keyword arguments
#1 positional and a sequence
#1 positional and artitrary keyword arguments
