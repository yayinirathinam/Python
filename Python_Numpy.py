#!/usr/bin/env python
# coding: utf-8

# In[33]:


import numpy as n
import pandas as pd


# In[40]:


l = [4,6]
print("Avg:",n.average(l))
print("Subtraction:", n.subtract(6,3))
print("Multiply:", n.multiply(6,3))
print("Div:", n.divide(6,3))
print("add:", n.add(6,3))

arr = n.array([
                [1,2,3],
              ['a','b','c']
                  ])

arr1 = n.array([
                [1,2,3],
              ['a','b','c'],
              [-4,-5,-6 ]
                  ])
print(arr[0])
print(arr[0][0])
print(arr1[0])
print(arr1[2][2])

df = pd.read_excel("C:\\Users\\yayin\\OneDrive\\Python\\2393276-Bike_Data.xlsx")
df["Color_New"] = n.where(df["Color"] == "Red","R","G")
df.head(10)


# In[ ]:




