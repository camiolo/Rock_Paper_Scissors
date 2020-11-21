
#!/usr/bin/env python3

# This is a fun game of Rock, Paper, Scissors for the kids!

from random import randint

 

# This creates a list of selections to choose from

t = ["rock", "paper", "scissors"]

 

# These are some instructions

print("Welcome to Rock, Paper, Scissors!  "

      "\nThe game will ask for your choice, be sure to type in all lowercase letters.  "

      "\nWhen you want to end the game you can simply type end.  "

      "\nEnjoy!")

 

# This will set the condition to True creating a loop, see if you can beat the computer.

while True:

    computer = t[randint(0,2)]

    player = input("rock, paper, scissors?")

    if player == computer:

        print("It's a tie!")

    elif player == "rock":

        if computer == "paper":

            print("You lose!", computer, "covers", player)

        else:

            print("You win!", player, "smashes", computer)

    elif player == "paper":

        if computer == "scissors":

            print("You lose!", computer, "cut", player)

        else:

            print("You win!", player, "covers", computer)

    elif player == "scissors":

        if computer == "rock":

            print("You lose!", computer, "smashes", player)

        else:

            print("You win!", player, "cuts", computer)

    elif player == "end":

        break

    else:

        print("You have not picked a valid option, please check your spelling and try again!")
