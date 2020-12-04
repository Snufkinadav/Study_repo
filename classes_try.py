import random
#CLASS DEFINITION
class User:
    rand = str(random.random())

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = first.lower() + '.' + last.lower() + '@company.co.uk'
        self.id = User.rand[-7:-1]
        
#FUNCTIONS

#TAKING A FULL NAME  
def take_name():
    #ASKING FOR NAME
    input_name = input('Please write your full name: ')
    #CONVERTING A NAME INTO A LIST
    split_name = input_name.split()
    #print(split_name)
    return list(split_name)
     
#CALLING take_name FUNCTION AND SETING NAME
new_user = take_name()

#PASSING NAME INTO CLASS
new_user = User(new_user[0],new_user[1])

#PRINTING CLASS __DICT__
print(new_user.id)








#OUTPUT
# print(new_user.last)
# print(new_user.email)