row1 = ['','','',]
row2 = ['','','',]
row3 = ['','','',]

def display(row1,row2,row3):
    print(row1)
    print(row2)
    print(row3)

display(row1,row2,row3)

def user_coice():
    #VRAIABLES

    #initial
    choice = 'Wrong'
    acceptable_range = range(0,10)
    within_range = False

    #TWO CONDITION TO CHECK
    #DIGIT OR WITHIN_RANGE == FALSE

    while (choice.isdigit() == False) or (within_range == False):
        choice = input('Please enter a number (0-10): ')

        if choice.isdigit() == False:
            print(f"Sorry, {choice} is not a digit")
        
        #RANGE CHECK
        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                within_range == False
                print(f"Sorry, {choice} is out of range (0-10)")

    return int(choice)

user_coice()