'''
Created on Aug 26, 2021

@author: osboxes
'''

class Lunch:
    def __init__(self):
        self.customer = Customer()
        self.employee = Employee()
        
    def order(self, foodName):
        print('Order: ', foodName)
        self.customer.placeOrder(foodName, self.employee)

    def result(self):
        self.customer.printFood()

class Customer:
    def __init__(self):
        self.food = None
        
    def placeOrder(self, foodName, employee):
        print('Order is placed')
        self.food = employee.takeOrder(foodName)
    
    def printFood(self): print(self.food.name)

class Employee:
    def takeOrder(self, foodName):
        print('Order is taken')
        return Food(foodName)

class Food:
    def __init__(self, name):
        self.name = name

if __name__ == '__main__':
    lunch = Lunch()
    lunch.order("Pizza Margarita")
    lunch.result()