# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 19:25:01 2018

@author: Sharmin
"""

#While loop
i = 1
while i<=10:
    print(i)
    i+=1

i = 1
while i<=10:
    print(i,end="\t")
    i+=1

#for loop
for i in range(1,11):
    print(i)

for i in range(1,11):
    print(i,end=" ")

#nested for loop
for i in range(1,6):
    for j in range(1,6):
        print(j)

for i in range(1,6):
    for j in range(1,6):
        print(j,end=" ")
    print()