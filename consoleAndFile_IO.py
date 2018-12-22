# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 00:59:16 2018

@author: Sharmin
"""

#Console I/O
inp = input("Enter a number:")
number1 = int(inp)

inp = input("Enter the second number:")
number2 = int(inp)

print(number1 + number2)

#file I/O
inp = input("Enter some text here:")
with open("textfile.txt","w") as f:
    f.write(inp)

#file I/O
inp = input("Enter some text here:")
with open("textfile.txt","a") as f:
    f.write(inp)
    
#file I/O

with open("textfile.txt","r") as f:
    print(f.read())