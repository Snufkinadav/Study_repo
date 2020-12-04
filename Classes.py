import random

class Employee:
    """Createing User class, follwing yt=https://www.youtube.com/watch?v=ZDa-Z5JzLYM"""
    pay_raise = 1.04
    pay = 0
    num__of_emps = 0

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last +'@company.com'
        Employee.num__of_emps += 1
        #From here it's my own try and error
        

    def apply_raise(self):
        self.pay = int(self.pay * self.pay_raise)
        #From here it's my own try and error
    
    def full_name(self):
        print(f'{self.first} {self.last}')
        #From here it's my own try and error

user1 = Employee('Dor','Nadav',50000)
user2 = Employee('Graham','Adkins-Nadav',60000)

print(Employee.num__of_emps)


# user1.pay_raise = 1.06

# print(Employee.pay_raise)
# print(user1.pay_raise)
# print(user2.pay_raise)

# print(Employee.pay)
# print(user1.pay)
# print(user2.pay)
# print(user1.pay)
# print(user1.full_name())
# print(user1.email)
# print(user2.email)
# print(user1.full_name())
# print(user2.full_name())