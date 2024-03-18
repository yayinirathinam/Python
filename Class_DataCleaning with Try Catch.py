#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd

try:
    df = pd.read_excel("C:\\Users\\yayin\\OneDrive\\Python\\2393276-Bike_Data.xlsx")
    
    class DataCleansing:
        def __init__(self, df):
            self.df = df

        def row_col_cnt(self):
            try:
                print("Row_column count check:")
                return self.df.shape
            except Exception as err_count:
                print(err_count)
                return 0

        def remove_dups(self):
            print("Remove duplicates:")
            self.df = self.df.drop_duplicates()
            return self.df

        def list_isna(self):
            print("Check isna:******")
            return list(self.df.isna())

        def list_isnull(self):
            print("Check isnull:******")
            return list(self.df.isnull())

        def remove_na(self):
            print("Remove_na:******")
            self.df = self.df.dropna()
            return self.df

        def list_cols(self):
            print("Columns:******")
            return list(self.df.columns)

    getdata = DataCleansing(df)
    print(getdata.row_col_cnt())
    print(getdata.list_cols())
    print(getdata.list_isna())
    print(getdata.list_isnull())
    print(getdata.remove_dups())
    print(getdata.remove_na())
    print(getdata.row_col_cnt())

except Exception as e1:
    print(e1)




# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




