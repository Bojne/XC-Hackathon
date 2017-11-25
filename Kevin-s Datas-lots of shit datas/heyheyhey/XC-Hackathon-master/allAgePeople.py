
# coding: utf-8

# In[3]:


import pandas as pd
import matplotlib 
import matplotlib.pyplot as plt
import xlrd
import numpy as np


# In[15]:


pf = pd.read_excel("./Data/y02-01.xls")
df =pd.DataFrame(pf)
df1 = df[2:]
df1.head()


# In[16]:


df1.tail(20)


# In[58]:


df2 = df1[128:129]
for row in df2:
    df3 = df2.set_index(str(row)).T
df3 = df3[4:]
df3


# In[76]:


get_ipython().run_line_magic('matplotlib', 'inline')
df4 = df3.astype(float)
df4.plot.line()
print(df4[0:1],df4[15:16],df4[17:18])


# #### 

# In[69]:


print (df3.plot.bar())


# 
# 
