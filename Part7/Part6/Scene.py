'''
Created on Aug 29, 2021

@author: osboxes
'''

class Scene:
    def __init__(self):
        self.customer = Customer()
        self.clerk = Clerk()
        self.parrot = Parrot()
        
    def action(self):
        print('Activate nested objects')
        self.customer.line()
        self.clerk.line()
        self.parrot.line()

class Customer:
    def line(self): print("customer: that's one ex-bird!")

class Clerk:
    def line(self): print("clerk: no it isn't...")

class Parrot:
    def line(self): print("parrot: None")
