#!/usr/bin/env python
# coding: utf-8

# In a jupyter notebook solve the following question using both python and SQL. Please upload the notebook to GitHub and provide the link submission box below.
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | id            | int     |
# | recordDate    | date    |
# | temperature   | int     |
# +---------------+---------+
# id is the column with unique values for this table.
# This table contains information about the temperature on a certain day.
# 

# In[1]:


import sqlite3


# In[2]:


conn = sqlite3.connect('weather.db')
cur = conn.cursor()


# In[3]:


data = [
    (1, '2024-02-19', 10),
    (2, '2024-02-20', 15),
    (3, '2024-02-21', 20),
    (4, '2024-02-22', 25)
]


# In[ ]:




