# -*- coding: utf-8 -*-
"""Pyspark_Denserank&Rowno.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RhrwR-xt2_aWpWYgg0VMvVGAk2-AeofI
"""



!pip install pyspark

import  pyspark

from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
c = pyspark.SparkConf().setAppName("test_app").setMaster("local")
sc = pyspark.SparkContext(conf = c)
spark = SparkSession(sc)

from pyspark.sql.functions  import  *
from pyspark.sql.window import Window
from pyspark.sql.functions import asc,desc
from pyspark.sql.functions import dense_rank
from pyspark.sql.functions import row_number

data = [
        (1, "Karthi",80,"NC"),
        (2, "Amy",80,"NY"),
        (3, "Jack",94,"NY"),
        (4, "Camellia",40,"NC"),
        (5, "Lucy",90,"NY"),
        (6,"Thomas",50,"NY"),
        (7,"Erwin",45,"NC"),
        (8,"Jones",45,"NC")
       ]
column = ["Id","Name","Mark","City"]
df = spark.createDataFrame(data,column)
df.show()

##winres = Window().orderBy(desc("Mark"))
winres = Window.partitionBy("City").orderBy(desc("Mark"))
df = df.withColumn("dense_rank",dense_rank().over(winres))

df = df.withColumn("Row_No", row_number().over(winres))
df.show()