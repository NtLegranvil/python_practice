"""
Guess The Number Game
"""

# The objective of the game is to guess the hidden number

print("Hello, do you want to play a game?", "[y/n]")

user = input() #takes input from user and converts it into a string

if user == 'n':
    print("Well, you don't know me, but I know you, and I wanna play a game.")
    print("Now I'll ask you one more time, Make the correct choice.", "[y/y]")
    user = input()
    
if user == 'y':
    print("There's only one way to win this game, and it's to guess my secret number.\nYou better hurry up, live or die.")

import random # import library to generate random numbers for program

hidden_num = random.randint(0,100) # random integer from 0 to 100

num = int(input("Guess the number: ")) # enter number to guess

while num != hidden_num: # if guess is not equal to hidden number the loop will begin
    print("Think hard. The number is in the back of your mind. ") # first output message received for being incorrect
    num = int(input("Try again: ")) # if incorrect again loop will start from the top
    if num != hidden_num:
        print("Suffering? You haven't seen anything yet.")
    
if num == hidden_num:
    print("The secret number is:", hidden_num,"\nGAME OVER.") # once hidden number is found this will be the final output
