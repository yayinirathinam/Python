#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
data1 = pd.read_excel("C:\\Users\\yayin\\OneDrive\\Python\\Car_data_NullValues.xlsx")
data1.head(5)


# In[167]:


#create a new DF
data2 = data1[["Year","Selling_Price","Present_Price"]]
data2.tail(5)
#group by
data2.groupby("Year")["Selling_Price"].sum()
data2.groupby("Year")["Selling_Price"].mean()
data2["Selling_Price"].mean()
data2["Selling_Price"].sum()
data2["Selling_Price"].min()
data2["Selling_Price"].max()

#group by with alias name
data3 = data1.groupby("Year")[["Selling_Price"]].sum()
data3 = data3.rename(columns={"Selling_Price":"Sum"})
data3

#group by on multiple columns and different functions on different attributes
data5= data1.groupby(["Year","Car_Name"]).agg({"Selling_Price":"min","Kms_Driven":"sum"}).head(5)

#group by on multiple columns and different functions on same attributes + different attributes
data5 = data1.groupby(["Year","Car_Name"]).agg({"Selling_Price":"sum","Kms_Driven":["min","max"]})

#Sorting
data5.sort_values("Year",ascending=False)

###***********Different Filter method*************************

### this displays true or false values based on the filter condition not value
[data1["Year"] == 2018]

##this give the values matching the filter
## select "Car_Name","Kms_Driven" from data1 where year = 2018 and Transmission = "Manual"

data1[["Car_Name","Kms_Driven"]][(data1["Year"] == 2018) & (data1["Transmission"]=="Manual")]

## select * from data1 where year = 2018 and Transmission = "Manual"
data1[(data1["Year"] == 2018) & (data1["Transmission"]=="Manual")]

###same filter with data query moethod

data1.query("Year == 2018" and "Transmission == 'Manual'")
data1.query("Year == 2018" and "Transmission == 'Manual'")[["Car_Name","Kms_Driven"]]

#Same filter with Loc
data1.loc[(data1["Year"] == 2018) & (data1["Transmission"]=="Manual")][["Car_Name","Kms_Driven"]]
data1.loc[(data1["Year"] == 2018) & (data1["Transmission"]=="Manual")]


#Assignment add/ subtract 2 cols and then sort it
data1["Profit"] = data1["Present_Price"]-data1["Selling_Price"]
data1.sort_values("Year", ascending= False)





# In[ ]:




