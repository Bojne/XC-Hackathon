
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib 
import matplotlib.pyplot as plt
import xlrd
import numpy as np


# In[3]:


pf = pd.read_excel("./Data/105_base0.xls")
df =pd.DataFrame(pf)
df1 = df[2:]
df1.head()


# In[25]:


df1.columns = ['c1','c2','c3','c4','c5','c6','c7','c8','c9','c10','c11','c12','c13','c14','c15','c16','c17']
df1
df2 = df1[2:]
df3 = df2.astype(float)
df3.sum()

