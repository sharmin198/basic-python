# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 19:39:11 2018

@author: Sharmin
"""

#loop control system

#break statement

for i in range(1,10):
    if(i>5):
        break
    print(i)

#control statement
for i in range(1,11):
    if(i>5 and i<8):
        continue
    print(i)

#pass statement
i = 1
if(i==1):
    pass
else:
    pass