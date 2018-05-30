# -*- coding: utf-8 -*-
"""
Created on Mon May 28 11:41:37 2018

@author: D
"""
# prints the word backwards
fruit = "banana"
length_fruit = len(fruit)
index = length_fruit
count = 0

# takes each letter of the word and prints on a separate line in reverse order
while  count < length_fruit:
    letter = fruit[index -1]
    print (letter)
    index = index - 1
    count = count +1
    
# defines the function
def fun_with_fruit(fruit, a_letter):
    word = fruit
    count = 0
    print("The name of the fruit is: ", fruit, "and the letter is: ", a_letter)
    for letter in word:
        if letter == a_letter:
           count = count + 1
# checks for grammar
    if count == 1:
        print("The total number of", a_letter,"'s in", fruit, "is:", count)
    else: 
        print("The total number of", a_letter,"'s in", fruit, "are:", count)

# calls the function
fun_with_fruit("banana", 'n')
fun_with_fruit("strawberry", 'r')
fun_with_fruit("kiwi", 'k')
