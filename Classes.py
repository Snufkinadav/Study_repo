import random
import datetime

class Employee:
    """Createing User class, follwing yt=https://www.youtube.com/watch?v=ZDa-Z5JzLYM"""
    pay_raise = 1.04
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

    @classmethod
    #changing methods of class - NO NEED TO PASS CLASS ONCE cls IS SET
    def set_raise_amt(cls, amount):
        cls.pay_raise = amount 
    
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
        

user1 = Employee('Dor','Nadav',50000)
user2 = Employee('Graham','Adkins-Nadav',60000)

my_date = datetime.date(2016, 7, 11)

print(Employee.is_workday(my_date))








# emp_str_1 = 'David-Math-70000'

# new_emp_1 = Employee.from_string(emp_str_1)

# print(new_emp_1.__dict__)

# print(Employee.num__of_emps)

# print(new_user_1)

# new_user_1 = Employee(first, last, pay)
# # user1.pay_raise = 1.06
# Employee.set_raise_amt(1.05)

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