import random

class User:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = first.lower() + '.' + last.lower() + '@company.co.uk'

#attempt to take a string of a name and break it down to email
input_name = input('please write your full name: ')
full_name = input_name.split()
user1 = User(full_name[0], full_name[1])

print(user1.last)

#print(user1.email)