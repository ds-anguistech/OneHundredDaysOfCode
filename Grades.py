# -*- coding: utf-8 -*-

# Spyder Editor


tenths = input("Please enter a number between 0 and 1:  ")
score = float(tenths)

while score > 1:
    print("That is not a valid response!")
    tenths = input("Please enter a number between 0 and 1:  ")
    score = float(tenths)

if score >= 0.9:
    print("You made an A!")
elif score >=0.8:
    print("You made a B")
elif score >= 0.7:
    print("You made a C")
elif score >= 0.6:
    print("You made a D :-P")
elif score < 0.6:
    print("You failed! You got an F!")
    
    