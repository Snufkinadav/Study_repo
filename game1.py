from random import shuffle

def shuffle_list(i):
    shuffle(i)
    return i

def player_guess():
    guess = ''
    while guess not in ['0','1','2']:
        guess = input("Hey you!\nLet's play a game,\nChoose a number 0,1 or 2: ")
        return int(guess)

def check_guess(mylist,guess):
    if mylist[guess] == 'O':
        print("Well Done!, you are right!")
        print(mylist)
    else:
        print("Nope, this is not what I chose!")
        print(f"my choise was {mylist}")


def_list = ['','O','']
mix_list = shuffle_list(def_list)
guess = player_guess()
check_guess(mix_list,guess)