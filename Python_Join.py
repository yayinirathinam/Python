#!/usr/bin/env python
# coding: utf-8

# In[59]:


import pandas as pd
df_emp = pd.read_excel("C:\\Users\\yayin\\OneDrive\\Python\\2398498-Emp_Training_Data.xlsx");
df_tra = pd.read_excel("C:\\Users\\yayin\\OneDrive\\Python\\2398497-Training.xlsx");
df_car_null = pd.read_excel("C:\\Users\\yayin\\OneDrive\\Python\\Car_data_NullValues.xlsx");
df_car = pd.read_excel("C:\\Users\\yayin\\OneDrive\\Python\\Car_data.xlsx");

df_tra[["Employee_ID","Supplier"]];
df_emp[["EmployeeID","Dept","Title"]];


#### Merge - join

df_join = pd.merge(df_emp,df_tra,right_on = "Employee_ID",left_on = "EmployeeID",how = "inner")
d1 = df_join[df_join["Dept"]== "Sales" ];
d1

### Merge - Join with select filters
df_join = pd.merge(df_emp,df_tra,right_on = "Employee_ID",left_on = "EmployeeID",how = "inner").query(("Dept == 'Sales'"))
df_join[["EmployeeID","MaritalStatus","Course Name"]].sort_values("EmployeeID")
d2 = df_join[["Course Name"]].drop_duplicates("Course Name").sort_values("Course Name")
d2.count()
d2.shape

'''
Merge - Join with select filters with same/ amboguity columns - sufix
filter using query and NAN
selected cols''' 

d3 = pd.merge(df_car,df_car_null,on = "Car_Name", how = "inner",suffixes=("_org","_cpy")).query("Car_Name == 'swift' & Transmission_cpy.isnull()")[["Car_Name","Transmission_org","Transmission_cpy"]]
d3






# In[ ]:




