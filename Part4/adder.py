def adder1(a,b): return a+b

def adder2(*a):
    sum = a[0]
    for x in a[1:]:
       sum +=  x
    return sum

def adder3(good=10,bad=100,ugly=1000):
    return good+bad+ugly

def adder(**kargs):
    sum = list(kargs.values())[0]
    for next in list(kargs.values())[1:]:
        sum += next
    return sum

# print(adder("hi", "there"))
# print(adder(1.0,2.0))
# print(adder([1,2],[3]))
# print(adder(1))
print(adder(good=1,bad=2,ugly=3,super=1000))