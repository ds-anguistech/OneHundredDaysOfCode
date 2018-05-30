# -*- coding: utf-8 -*-
"""
Created on Sat May 26 13:10:38 2018

@author: D
"""
# prize is number you're looking for
prize = 5

# make a guess
guess = input("Pick a number between 1 and 10:  \n")
guess = int(guess)

while prize != guess:
    if guess > prize:
        print("Your guess is too high")
        guess = input("Pick a number between 1 and 10:  \n")
        guess = int(guess)
    elif guess < prize:
        print("Your guess is too low")
        guess = input("Pick a number between 1 and 10:  \n")
        guess = int(guess)
print("You Picked Correctly! Congratulations!")