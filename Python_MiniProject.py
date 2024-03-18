#!/usr/bin/env python
# coding: utf-8

# In[34]:


import pandas as pd

df1 = pd.read_excel("C:\\Users\\yayin\\OneDrive\\Python\\2412624-2318028-investment_banking1.xlsx");
df1[['City','State']] = df1['city'].str.split(',',expand=True)

#In pandas, we should mention the axis as 1 to drop any columns, axis = 0 means row, axis 1 means cols

#df1 = df1.drop('City', axis=1)
#df1 = df1.drop('State', axis=1)
df1['State'] = df1['State'].str.strip()
print("Is there state code >len 3:", df1[df1['State'].str.len()>2]['State'].count())
print("*****************Data Sample of Investment Banking*********************************")
print(df1.head(5))


# to get aggregated lemvalues
df2 =  df1.groupby(["broker_type"]).agg({"broker_id":"count","firm_sales":sum,"global_sales":sum}).sort_values("broker_type", ascending = False).reset_index()

#renaming the cols
df2 = df2.rename(columns={"broker_id":"No_of_Brokers","firm_sales":"Sum_firm_sales", "global_sales" :"Sum_global_sales"})

## to classify the customer
def find_customer(row,fs,gs):
    if fs == 0 and gs != 0:
        return "Not a customer"
    elif fs != 0 and gs == 0:
        return "Privileged customer"
    elif fs != 0 and gs != 0:
        return "Progressive customer"
    else:
        return "Not initiated business"
    
    
df1["cust_type"] = df1.apply(lambda row: find_customer(row,row['firm_sales'], row['global_sales']), axis=1)

print("***************Aggregated values based on Broker Type*******************")
print(df2)
###df2.nunique()
print("")
print("***********************Type of customer based on Sales********************************")
print(df1[['broker_id','broker_type','cust_type','firm_sales','global_sales']].head(5))

print("")
print("*********************Count of brokers based on cust_type***************************")
df4 = df1.groupby(["cust_type"])[["broker_id"]].count().reset_index()
df4 = df4.rename(columns={"broker_id":"Count_of_broker_id"})
print(df4)

print("")
print("*********************Count of Cust_type based on cust_type,City***************************")
df3 = df1.groupby(["State","City","cust_type"])[["broker_id","broker_type"]].count().reset_index()
df3 = df3.rename(columns={"broker_id":"Count_of_broker_id","broker_type":"Count_of_broker_type"})
print(df3)
  





# In[ ]:





# In[ ]:





# In[ ]:




