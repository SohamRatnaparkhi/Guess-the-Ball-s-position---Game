from math import fabs
from random import shuffle

mylist = ['__', '__', 'o']
sl = []

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

def player_guess():
    guess = ''
    while guess not in ['1', '2', '3']:
        guess = input("\nEnter the position where the ball might be after shuffling the places- ")
    return int(guess)

def posn_check(guess, mylist):
    index = guess - 1
    if mylist[index] == 'o':
        return True
    else:
        return False

def restart_game(result):    
    if (result == False):
        print("\n-------------------------\nYou lost the game\n-------------------------\n")
        print("Position of ball is : ")
        '''restart = input("\nDo you want to Play Again\nIf yes click y\nIf no click n")
        if (restart == 'y'):
            main()
        else:
           return "GAME OVER"
         '''  
    else:
        print("\n-------------------------\nYou WON the game\n-------------------------\n")
        print("Position of ball is : ")
        '''print(sl)
        restart = input("\n\nDo you want to Play Again\nIf yes click y\nIf no click n\nDecision :- ")
        if (restart == 'y'):
            main()
        else:
           return "GAME OVER"
        '''

def main():
    mylist = ['__', '__', 'o']
    print("\n-------------------------\nGAME STARTS\n-------------------------\n")
    print("Current position of ball is : ")
    print(mylist)
    sl = shuffle_list(mylist)
    #print(sl)
    g = player_guess()
    result = posn_check(g, sl)
    restart_game(result)

    print(sl)
    restart = input("\nDo you want to Play Again\nIf yes click y\nIf no click n\nDecision :- ")
    if (restart == 'y'):
        main()
    else:
        return "GAME OVER"
    

main()


