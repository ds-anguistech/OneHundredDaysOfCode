# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

a = 12345.23567
print('%.0f'%a)
print ("Change since yesterday: %+.3f" % 1.5)
print("Todays temperature will be: %.3f" % 7.25)

data = ("John", "Doe", 53.44)
format_string = "Hello"

mystring = "hello"
myfloat = 10.0
myint = 20

print("String: %s" % mystring)
print("Float: %.1f" % myfloat)
print("Integer: %d" % myint)
print(data [0])
print(format_string, data[0], data[1], ". Your daily balance is:", data[2])
print(format_string, "%s" % data[0])


numbers = [] #creates an empty list
strings = []
names = ["John", "Eric", "Jessica"] #creates a list with three things in it

numbers.append(1) #adds numbers to the numbers list
numbers.append(2)
numbers.append(3)
strings.append("hello") #adds words to the strings list
strings.append("world")
second_name = names[1] #stores the second item in names list to the variable

print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)
