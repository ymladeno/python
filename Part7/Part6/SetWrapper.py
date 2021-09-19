'''
Created on Aug 16, 2021

@author: osboxes
'''
class Set:
    def __init__(self, value = []):
        self.data = []
        self.concat(value)
        
    def intersect(self, other):
        # print('Set.self.data: ', self.data)
        # print('Set.intersect: ', other)
        res = []
        for x in self.data:
            if x in other:
                # print('append: ', x)
                res.append(x)
        return Set(res)

    def union(self, other):
        res = self.data[:]
        for x in other:
            if not x in res:
                res.append(x)
        return Set(res)

    def concat(self, value):
        for x in value:
            if not x in self.data:
                self.data.append(x)

    def __len__(self):          return len(self.data)
    def __getitem__(self, key): print('getitem'); return self.data[key]
    def __and__(self, other):   return self.intersect(other)
    def __or__(self, other):    return self.union(other)
    def __repr__(self):         return 'Set:' + repr(self.data)
    def __iter__(self):         print('iter'); return iter(self.data)
    def __getattr__(self,name): 
        print('getattr: %s'  % (name))
        return getattr(self.data, name)

class SetSub(Set):
    def intersect(self, *other):
        s = Set(self.data)
        print('other:', other)
        print('len=%d' % len(other))
        res = s.intersect(other[0])
        for seq in other[1:]:
            res = res.intersect(seq)

        return res

    def union(self, *other):
        s = Set(self.data)
        res = s.union(other[0])
        for seq in other[1:]:
            res = res.union(seq)
        return res

    def __and__(self, *other):   return self.intersect(*other)
    def __or__(self, *other):    return self.union(*other)
    