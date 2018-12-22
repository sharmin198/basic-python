# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 20:01:04 2018

@author: Sharmin
"""

#tuples
#same as list but immutable
#stays in first bracet
tuple = (12,)
#if in any tuple has one element then after the element we have to put comma
#otherwise it will be counted as an integer number type
#if we put comma after the element then its type will be counted as tuple type
tuples = (12)
#after executing the above statement we will see that it will counted as an integer type
tuple1 = (11,123.122213,"it is a tuple element")
tuple2 = ("a string",123,2324.23)
tuple3 = tuple1+tuple2
tuple4 = tuple2+tuple1

print(tuple1[2])
print(len(tuple4))

for index in range(0,len(tuple1)):
    print(tuple1[index])

for index in tuple3:
    print(index)