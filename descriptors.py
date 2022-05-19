class Name:
    def __get__(self, instance, owner):
        print('fetch ...')
        return instance._name

    def __set__(self, instance, value):
        print('change ...')
        instance._name = value

class Person:
    def __init__(self, name):
        self._name = name
    name = Name()

bob = Person('Bob Smith')
print(bob.name)