row1 = ['','','',]
row2 = ['','','',]
row3 = ['','','',]

def display(row1,row2,row3):
    print(row1)
    print(row2)
    print(row3)

display(row1,row2,row3)

def user_coice():
    choice = 'Wrong'
    while choice.isdigit() == False:
        choice = (input('Please enter a number (0-10): '))

        if choice.isdigit() == False:
            print(f'Sorry, {choice} is not a digit')
    return int(choice)

user_coice()