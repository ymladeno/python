'''
Created on Aug 27, 2021

@author: osboxes
'''

class Animal:
    def speak(self):
        print('Animal.speak')
        
    def reply(self): 
        print('Animal.reply: calls')
        self.speak()
    
class Mammal(Animal):
    def speak(self):
        print('Mammal.speak')

class Cat(Mammal):
    def speak(self):
        print('Cat.speak')
        
class Dog(Mammal):
    def speak(self):
        print('Dog.speak')
        
class Primate(Mammal):
    def speak(self):
        print('Primate.speak')

class Hacker(Primate): pass
    # def speak(self):
        # print('Hacker.speak')

if __name__ == '__main__':
    spot = Cat()
    spot.reply()
    data = Hacker()
    data.reply()