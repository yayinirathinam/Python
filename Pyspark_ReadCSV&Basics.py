#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pyspark


# In[7]:


from pyspark.sql.functions import *
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
c = pyspark.SparkConf().setAppName("test_app").setMaster("local")
sc = pyspark.SparkContext(conf = c)
spark = SparkSession(sc)


# In[40]:


pys = spark.read.csv("C:\\Users\\yayin\\OneDrive\\Python\\2390704-Car_dataT.csv",header=True,inferSchema = True)
##type(pys)
##pys.show(5)
##pys.count()
##len(pys.columns)
pys.columns
##pys[["Car_Name","Present_Price"]].show(5)
##pys.select("Car_Name","Present_Price").show(5)
pys.select("Car_Name","Present_Price","Fuel_Type","Year").filter((col("Year")==2014) & (col("Fuel_Type")=="Petrol")).show(5)
pys.select("*").orderBy(col("Year").desc(),col("Kms_Driven").desc()).show(5)
pys.printSchema()


# In[ ]:





# In[ ]:




