# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 01:13:02 2018

@author: Sharmin
"""

#function (block of meaningful code)

def functionName(arg1,arg2):
    print(arg1,arg2)

functionName(12,"this is arg2")

def sumOfNumbers(num1,num2):
    return num1+num2

print(sumOfNumbers(12.33,23))

def length(l):
    count = 0
    for i in l:
        count+=1
    return count

print(length(['apple','banana','orange']))