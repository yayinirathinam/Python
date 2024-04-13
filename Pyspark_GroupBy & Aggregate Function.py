#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pyspark


# In[2]:


from pyspark.sql.functions import *
from pyspark.sql.functions import asc,desc

from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
c = pyspark.SparkConf().setAppName("test_app").setMaster("local")
sc = pyspark.SparkContext(conf = c)
spark = SparkSession(sc)


# In[11]:


pys = spark.read.csv("C:\\Users\\yayin\\OneDrive\\Python\\2390704-Car_dataT.csv",header=True,inferSchema = True)
##pys.show(5)
print("*******************Count Function with Distinct and Without Distinct**************************************")
print("Count of cars in 2014:", pys.select("Car_Name").filter(col("Year")==2014).count())
print("Count of distinct cars in 2014:", pys.select("Car_Name").filter(col("Year")==2014).distinct().count())
print("*************Group  BY count and Sorting*****************************")
pys.groupby("Year","Fuel_Type").count().show()
print("")
pys.groupBy("Year","Fuel_Type").count().sort(col("Year")).show()
print("")
print("*************Group  BY count and Sorting in descending*****************************")
pys.groupBy("Year","Fuel_Type").sum("Selling_Price").sort("Year", ascending=False).show()
print("******************Group By Aggregate with different types of sort & Countdistinct in agg function & filter***************************")
pys.groupBy("Year","Fuel_Type").agg(sum("Selling_Price").alias("SUM"),
                                avg("Kms_Driven").alias("Avg") 
                                   ).sort(col("Year").desc()).show()

pys.groupBy("Year","Fuel_Type").agg(sum("Selling_Price").alias("Sum of S_price"),
                                avg("Kms_Driven").alias("Avg"), 
                                max("Kms_Driven").alias("Highest Km"),
                                min("Kms_Driven").alias("Least Km"),                                                           
                                countDistinct("Car_Name").alias("No of Cars")
                                ).filter(col("No of Cars") > 10).sort("Year", ascending=False).show()


# In[ ]:




