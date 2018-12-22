# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 19:45:11 2018

@author: Sharmin
"""

#list : Non homogeneous collection of elements
list = [121324,1232.232,"it is a list element"]
print(list)
print(list[0])
print(list[1])
print(list[2])

#append : always add element at end of the list
list.append(10)

#insert : add element at any indeces of a list
list.insert(1,"adding element at 2nd position")

#updating list
list[2] = "something updated"
#deleting list element
#pop() function delete last element
list.pop()

#del keyword which delete any index of element
del list[3]

#length of a list
print(len(list))
for index in range(0,len(list)):
    print(list[index])

#another apporach of using for loop without using range
for index in list:
    print(index)