# class Person:
#     __slots__ = ['name', 'age']
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def __str__(self):
#         return 'Person: ' + self.name + ', ' + str(self.age)

# P = Person('Bob', 42)
# print(P)

class E:
    __slots__ = ['c', 'd']

class D(E):
    __slots__ = ['a']

X = D()
X.a = 1; X.c = 3
print(X.a, X.c)
print(X.__slots__, E.__slots__)