#!/usr/bin/env python
# coding: utf-8

# In[34]:


import pandas as pd

dict1  = {'Name':["Karthi"],'Address':["UK"],'number':['1231236688']}
myvar = pd.DataFrame(dict1)
##print(myvar)
myvar

## Lambda functions

add = lambda x,y,z: x+y+z
add(5,3,2)

concat_var = lambda Fname, Lname:(Fname+Lname)
concat_var("Karthi","yayini").upper()

#Lamda inside functions


def func_manipulate(x,y,z,action):
    result = action(x,y,z)
    return result

add = func_manipulate(5,5,2,lambda x,y,z: (x+y)*z*10)
sub = func_manipulate(5,5,2,lambda x,y,z: (x-y)*z*10)

## Lambda needs all parameters, but not required to be used in operations

Merg = func_manipulate("a","b","",lambda x,y,z:(x+y))
print("Addition: ", add)
print("Subtraction:", sub)###
print("Concat:", Merg)






# In[ ]:




