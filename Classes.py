import random

class Employee:
    """Createing User class, follwing yt=https://www.youtube.com/watch?v=ZDa-Z5JzLYM"""
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last +'@company.com'
        #From here it's my own try and error
        

    def pay_raise(self):
        self.pay = int(self.pay *1.10)
        #From here it's my own try and error
    
    def full_name(self):
        print(f'{self.first} {self.last}')
        #From here it's my own try and error

emp_1 = Employee('Dor','Nadav',50000)
emp_2 = Employee('Graham','Adkins-Nadav',60000)

emp_1.pay_raise()

print(emp_1.pay)
# print(emp_1.full_name())
# print(emp_1.email)
# print(emp_2.email)
# print(emp_1.full_name())
# print(emp_2.full_name())