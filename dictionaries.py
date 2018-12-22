# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 20:12:50 2018

@author: Sharmin
"""

#dictionaries
#key-value pairs
#dictionary specify with a curly braces
dictn = {}   #declaring a dictionary

dictn['apple'] = "Apple is a fruit"
dictn['orange'] = "Orange is a fruit"
dictn['car'] = "Cars are faster"
dictn['python'] = "python is a programming language"

print(dictn)

print(dictn['apple'])
print(dictn['orange'])
print(dictn['python'])

print(dictn.get('apple'))
print(dictn.get("apple"))

print(dictn.get("rose"))
#rose is a key which is not exist 
#but either here does not produce any error rather it print 'none'

#we also specify anything at the place of none

print(dictn.get("rose","the key is not exist"))
#now it print "the key is not exist"
#but if the key is exist it does not print such thing rather it print its value
print(dictn.get("orange","the key is not exist"))
#here as the key is exist here the value of the key orange will be printed

#deleting any key of a dictionary
del dictn["car"]

#finding the length of dictionary
print(len(dictn))

#finding list of the keys
listofKeys = list(dictn.keys())
#finding list of the values
listofvalues = list(dictn.values())

for key in dictn.keys():
    print(key)
    
for value in dictn.values():
    print(value)

