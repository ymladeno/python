'''
Created on Aug 8, 2021

@author: osboxes
'''

class Adder:
    def add(self, x, y): print("Not implemented")
    def __add__(self, y): return self.add(y)

class ListAdder(Adder):
    def __init__(self): self.data = []
    
    def add(self, y):
        self.data.append(y) 
        return self.data

class DictAdder(Adder):
    def __init__(self): self.data = {}

    def add(self, y):
        self.data.update({y: y})
        return self.data

