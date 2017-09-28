#!/usr/bin/python3
import random
#system choose random no play
n=(int(input("press 7 to play")))
#using 7 number to play
i=0
j=0
while(n==7):
    #put n=7
    t=["Rock","Paper","Scissors"]
    #3 choice to play with dice
    Computer=t[random.randint(0,2)]
    #randon number choose from 0 to2
    print("Enter your Choice:-")
    # using 3 choice rock paper sissors
    Player="False"
    Player=input("Rock, Paper, Scissors")
    if(Computer==Player):
        print("Tie!")
    elif(Computer=="Rock"):
        if(Player=="Paper"):
            print("The computer played: ",Computer)
            print("The Player played: ",Player)
            print("The Paper Wraps the Stone!")
            print("Player Wins!")
            #player won and computer chooses
            i=i+1
            #adding i + 1
        else:
            print("Computer Wins")
            j=j+1
            #adding j+1
    elif(Computer=="Paper"):
        if(Player=="Scissors"):
            print("The computer played: ",Computer)
            print("The Player played: ",Player)
            # player is playing
            print("The Scissors Cuts Paper!")
            print("Player Wins!")
            i=i+1
            # adding i +1
           
        else:
            print("Computer Wins")
            # computer wins
    else:
        print("Enter Choice again")
        # entering the choice
    if(i>j):
        print("Player leads by ",i-j)
        # player i-j
    elif(i==j):
        print("The Scores are tied ")
        # result
    else:
        print("Computer leads by ",j-i)
        #playing rock paper siscors
        #using computer
