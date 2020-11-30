from random import shuffle
 
def shuffle_l(x):
     shuffle(x)
     return x[0]

mylist = list(range(1,11))

x = shuffle_l(mylist)
print(x)