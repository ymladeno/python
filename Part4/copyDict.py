def copyDict(dict):
    newDict={}
    for key in list(dict.keys()):
        newDict[key] = dict[key]
    return newDict

d = {'a':1,'b':2,'c':3}
d1 = copyDict(d)
if d1 is not d:
    print("Copy succeed!")
