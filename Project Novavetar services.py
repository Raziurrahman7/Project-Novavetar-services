#!/usr/bin/env python
# coding: utf-8

# In[18]:


import numpy as np 
import pandas as pd 
sfPermits = pd.read_csv(r"C:\Users\razi2\Downloads\archive (1)\Youth_Tobacco_Survey__YTS__Data.csv")
np.random.seed(0)


# In[19]:


totalCells = np.product(sfPermits.shape)
missingCount = sfPermits.isnull().sum()
totalMissing = missingCount.sum()
print("The SF Permits dataset contains", round(((totalMissing/totalCells) * 100), 2), "%", "missing values.")


# In[20]:


sfPermits.sample(5)


# In[21]:


totalCells = np.product(sfPermits.shape)
missingCount = sfPermits.isnull().sum()
totalMissing = missingCount.sum()
print("The SF Permits dataset contains", round(((totalMissing/totalCells) * 100), 2), "%", "missing values.")


# In[23]:


missingCount[['Response']]


# In[25]:


print("Percent missing data in Response Suffix column =", (round(((missingCount['Response'] / sfPermits.shape[0]) * 100), 2)))


# In[26]:


sfPermits.dropna()


# In[27]:


sfPermitsCleanCols = sfPermits.dropna(axis=1)
sfPermitsCleanCols.head()


# In[28]:


print("Columns in original dataset: %d \n" % sfPermits.shape[1])
print("Columns with na's dropped: %d" % sfPermitsCleanCols.shape[1])


# In[30]:


imputeSfPermits = sfPermits.fillna(method='ffill', axis=0).fillna("0")


# In[31]:


imputeSfPermits.head()

