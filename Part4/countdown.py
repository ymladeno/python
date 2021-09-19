def countdown(a):
    if(a == 0):
        print('stop')
        return
    else:
        print(a, end=' ')
        countdown(a-1)
    
'''
Generator approach
gen = (x for x in range(10,0,-1))
list(gen)
'''