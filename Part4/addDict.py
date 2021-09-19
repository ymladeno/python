def addDict(dict1,dict2):
    new = {}
    for key in dict1:
        new[key] = dict1[key]

    for key in dict2:
        new[key] = dict2[key]
    return new

# def addList(list1,list2):
    # new = []
    # for next in list1:
        # new.append(next)
    # for next in list2:
        # new.append(next)
    # return new

def addList(list1,list2):
    return list1[:]+list2[:]

def addArgs(arg1,arg2):
    if type(arg1) != type(arg2):
        print("type mistach. Exit")
        return

    if  type(arg1) == dict:
        return addDict(arg1,arg2)
    
    if  type(arg1) == list:
        return addList(arg1,arg2)
    
    print("Unsupported type: ", type(arg1))

d1 = {'a':1}
d2 = {'a':1,'b':2}

print(addArgs(d1,d2),addArgs([1,2], [1,3]))
