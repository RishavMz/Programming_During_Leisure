# Author : RishavMz
# A simple tic tac toe game
# Two options , Human vs computer or human vs human

import random
player = 0
computer = 0
player1 = 0
player2 = 0

# This function checks if any player has won
def check(li):
    for i in range(3):
        if(li[i] == li[i+3] and li[i] == li[i+6]):
            return li[i]
    for i in [0,3,6]:
        if(li[i] == li[i+1] and li[i] == li[i+2]):
            return li[i]
    if(li[0] == li[4] and li[0] == li[8]):
        return li[0]
    if(li[6] == li[4] and li[6] == li[2]):
        return li[6]    
    return 0    

# Handles the code for Human vs computer
def comp():
    global player,computer
    li = [1,2,3,4,5,6,7,8,9]
    se = list()
    while(True):
        k = 0
        print("\n-------------------")
        for i in range(3):
            print('|' , end="  ")
            for j in range(3):
                print (li[k] , end = "  |  ")
                k+=1
            print("\n-------------------")
            if(k==8):
                break
        kk=0   
        # Check if tie 
        for a in range(9):
            if(li[a] == "0" or li[a] == "X"):
                kk+=1
        if(kk == 9):
            print("Its a tie")
            break            
        print('Select a box')
        while(True):
            # Player input
            box = int(input())    
            if(box not in se):
                li[box-1] = '0'
                se.append(box)
                break
            else:
                print("Select a valid box")

        kk=0    
        for a in range(9):
            if(li[a] == "0" or li[a] == "X"):
                kk+=1
        if(kk == 9):
            print("Its a tie")
            break             
        while(True):
            # Computer input
            l = random.randrange(1,10)
            if(l in se):
                continue
            else:
                li[l-1] = "X"
                se.append(l)
                break 
        # Checks if game over       
        value = check(li)    
        if(value == 0):
            continue
        elif value == "0":
            print("Player Wins!!!")
            player += 1
            break
        elif value == "X":
            print("Computer Wins!!!")  
            computer += 1
            break
    k = 0
    print("\n-------------------")
    for i in range(3):
        print('|' , end="  ")
        for j in range(3):
            print (li[k] , end = "  |  ")
            k+=1
        print("\n-------------------")
        if(k==8):
            break 
    # Displays final score       
    print("\nScore: \n \t Player" , player, "\n\tComputer", computer,"\n")
    print("Press 1 to play again, 2 to quit")
    c = int(input())
    if(c==1):
        # Another game
        comp()
    else:
        return    

# Handles the code for human vs human
def mano():
    global player1,player2
    li = [1,2,3,4,5,6,7,8,9]
    se = list()
    while(True):
        k = 0
        print("\n-------------------")
        for i in range(3):
            print('|' , end="  ")
            for j in range(3):
                print (li[k] , end = "  |  ")
                k+=1
            print("\n-------------------")
            if(k==8):
                break
        kk=0 
        # Check for tie   
        for a in range(9):
            if(li[a] == "0" or li[a] == "X"):
                kk+=1
        if(kk == 9):
            print("Its a tie")
            break            
        print('Select a box')
        while(True):
            # Player 1 input
            box = int(input())    
            if(box not in se):
                li[box-1] = '0'
                se.append(box)
                break
            else:
                print("Select a valid box")
        k = 0
        print("\n-------------------")
        for i in range(3):
            print('|' , end="  ")
            for j in range(3):
                print (li[k] , end = "  |  ")
                k+=1
            print("\n-------------------")
            if(k==8):
                break
        if(check(li) == "0"):
            print("Player1 Wins!!!")
            player1 += 1
            break   
        kk=0    
        for a in range(9):
            if(li[a] == "0" or li[a] == "X"):
                kk+=1
        if(kk == 9):
            print("Its a tie")
            break             
        while(True):
            # Player 2 input
            box = int(input())    
            if(box not in se):
                li[box-1] = 'X'
                se.append(box)
                break
            else:
                print("Select a valid box")
        # Check if game over   
        value = check(li)    
        if(value == 0):
            continue
        elif value == "0":
            print("Player1 Wins!!!")
            player1 += 1
            break
        elif value == "X":
            print("Player2 Wins!!!")  
            player2 += 1
            break
    k = 0
    print("\n-------------------")
    for i in range(3):
        print('|' , end="  ")
        for j in range(3):
            print (li[k] , end = "  |  ")
            k+=1
        print("\n-------------------")
        if(k==8):
            break    
    # Display final score    
    print("\nScore: \n \t Player1" , player1, "\n\t Player2", player2,"\n")
    print("Press 1 to play again, 2 to quit")
    c = int(input())
    if(c==1):
        # For another game
        mano()
    else:
        return             

# Code to run at rhe beginning of the application
print("Welcome to tic tac toe made by me.")
print("Enter 1 for player vs computer")
print("Enter 2 for player vs player")
choice = int(input())
if(choice == 1):
    comp()

elif(choice == 2):
    mano()
