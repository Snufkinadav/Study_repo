## DISPLAYING BOARD IN ARGUMENT
def display_board(board):
    row1 = board[1:4]
    row2 = board[4:7]
    row3 = board[7:10]
    print(row1)
    print(row2)
    print(row3)
test_board = ['0','1','2','3','4','5','6','7','8','9']
display_board(test_board)

## TAKE IN PLAYER'S CHOICE
def player_input():
    choice = 'wrong'
    acceptable_range = range(0,10)
    within_range = False
##CHECK TWO CONDITIONS
    ## IF INPUT IS DIGIT
    ## IF CHOICE WITHIN RANGE
    while (choice.isdigit() == False) or (within_range == False):
        choice = input("Choose a number to place your position")
        if choice.isdigit() == False:
            print("Sorry, invalid entry, please choose a number to place your position")
        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range == True
            else:
                within_range  = False
                print("Sorry, your choice is out of range")
            return int(choice)

def place_marker(board,marker,position):
        board[position] = marker

#place_marker(test_board,ply1[x],player_input[2])
