# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 01:39:10 2018

@author: Sharmin
"""

#basic list comprehension
list1 = [1,2,3,4,5,6,7,8,9]
list2 = []
#copying the list1 to list2 in general approach
for n in list1:
    list2.append(n)

#copying the list1 to list2 in list comprehension approach
list2 = [n for n in list1]
list2 = [n for n in list1 if n <=5]

list3 = [1,3,5,7,9]
list2 = [n for n in list1 if n not in list3]

list2  = [n*2 for n in list1]
list2 = [n for n in list1 if n%2==0]

#Generator comprehension
squaregen = (n**2 for n in list1)
list(squaregen)

dict1 = {'apple':1,'orrange':4,'banana':9}
newdict = {key:dict1[key] for key in dict1.keys()}
newdict = {key:dict1[key] for key in dict1.keys() if dict1[key] > 5}

words = ["I", "love", "you"]
sentence = " ".join(words)
sentence = ".".join(words)