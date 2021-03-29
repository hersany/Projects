#!/usr/bin/env python
# coding: utf-8

# <h1><p style="text-align: center;">Data Analysis with Python <br>Project - 1</p><h1> - Traffic Police Stops <img src="https://docs.google.com/uc?id=17CPCwi3_VvzcS87TOsh4_U8eExOhL6Ki" class="img-fluid" alt="CLRSWY" width="200" height="100"> 

# Before beginning your analysis, it is critical that you first examine and clean the dataset, to make working with it a more efficient process. You will practice fixing data types, handling missing values, and dropping columns and rows while learning about the Stanford Open Policing Project dataset.

# ***

# ## Examining the dataset

# You'll be analyzing a dataset of traffic stops in Rhode Island that was collected by the Stanford Open Policing Project.

# Before beginning your analysis, it's important that you familiarize yourself with the dataset. You'll read the dataset into pandas, examine the first few rows, and then count the number of missing values.

# **INSTRUCTIONS**
# 
# *   Import pandas using the alias ``pd``.
# *   Read the file police.csv into a DataFrame named ``ri``
# *   Examine the first 5 rows of the ``DataFrame`` (known as the ``"head"``).
# *   Count the number of missing values in each column: Use ``.isnull()`` to check which ``DataFrame`` elements are missing, and then take the ``.sum()`` to count the number of ``True`` values in each column.

# In[1]:


import pandas as pd


# In[2]:


pwd


# In[3]:


ri = pd.read_csv('police.csv', low_memory = False)


# In[4]:


ri.shape


# In[5]:


ri.info()


# In[6]:


ri.head()


# In[7]:


ri.isnull()


# In[8]:


ri.isnull().sum()


# ***

# ## Dropping columns

# Often, a DataFrame will contain columns that are not useful to your analysis. Such columns should be dropped from the ``DataFrame``, to make it easier for you to focus on the remaining columns.
# 
# You'll drop the ``county_name`` column because it only contains missing values, and you'll drop the ``state`` column because all of the traffic stops took place in one state (Rhode Island). Thus, these columns can be dropped because they contain no useful information.

# **INSTRUCTIONS**
# 
# *   Examine the ``DataFrame``'s shape to find out the number of rows and columns.
# 
# *   Drop the columns that almost consist of missing values. 
# 
# *   Examine the ``.shape`` again to verify that there are now two fewer columns.

# In[9]:


ri.shape


# In[10]:


ri.info()


# In[9]:


ri.drop(['state', 'county_name', 'county_fips', 'fine_grained_location'], axis = 1, inplace = True)


# In[10]:


ri.shape


# In[11]:


ri.info()


# ***

# ## Dropping rows

# When you know that a specific column will be critical to your analysis, and only a small fraction of rows are missing a value in that column, it often makes sense to remove those rows from the dataset.
# 
# During this course, the ``driver_gender`` column will be critical to many of your analyses. Because only a small fraction of rows are missing ``driver_gender``, we'll drop those rows from the dataset.

# **INSTRUCTIONS**
# 
# *   Count the number of missing values in each column.
# 
# *   Drop all rows that are missing ``driver_gender`` by passing the column name to the subset parameter of ``.dropna()``.
# *   Count the number of missing values in each column again, to verify that none of the remaining rows are missing ``driver_gender``.
# *   Examine the ``DataFrame``'s ``.shape`` to see how many rows and columns remain.

# In[12]:


ri.isnull().sum()


# In[13]:


ri.dropna(subset = ['driver_gender'], inplace = True)


# In[14]:


ri.shape


# ***

# ## Fixing a data type

# We know that the ``is_arrested`` column currently has the ``object`` data type. In this exercise, we'll change the data type to ``bool``, which is the most suitable type for a column containing ``True`` and ``False`` values.
# 
# Fixing the data type will enable us to use mathematical operations on the ``is_arrested`` column that would not be possible otherwise.

# **INSTRUCTIONS**
# 
# *   Examine the head of the ``is_arrested`` column to verify that it contains ``True`` and ``False`` values.
# *   Check the current data type of ``is_arrested``.
# *   Use the ``.astype()`` method to convert ``is_arrested`` to a ``bool`` column.
# *   Check the new data type of ``is_arrested``, to confirm that it is now a ``bool`` column.

# In[15]:


ri[['is_arrested']].head()


# In[18]:


ri['is_arrested'].dtype


# In[16]:


# ri = ri.astype({'is_arrested' : 'bool'}, copy = False)
ri['is_arrested'] = ri['is_arrested'].astype('bool')


# In[17]:


ri['is_arrested'].dtype


# ***

# ## Combining object columns

# Currently, the date and time of each traffic stop are stored in separate object columns: ``stop_date`` and ``stop_time``.
# 
# You'll combine these two columns into a single column, and then convert it to ``datetime`` format. This will enable convenient date-based attributes that we'll use later in the course.

# # **INSTRUCTIONS**
# 
# *    Use a string method to concatenate ``stop_date`` and ``stop_time`` (separated by a space), and store the result in ``combined``.
# *    Convert ``combined`` to ``datetime`` format, and store the result in a new column named ``stop_datetime``.
# *    Examine the ``DataFrame`` ``.dtypes`` to confirm that ``stop_datetime`` is a datetime column.

# In[18]:


ri.head()


# In[19]:


ri['stop_datetime'] = ri['stop_date'].str.cat(ri['stop_time'], sep = ' ')


# In[20]:


ri['stop_datetime'] = pd.to_datetime(ri['stop_datetime'])


# In[21]:


ri.dtypes


# The last step that you'll take in this chapter is to set the ``stop_datetime`` column as the ``DataFrame``'s index. By replacing the default index with a ``DatetimeIndex``, you'll make it easier to analyze the dataset by date and time, which will come in handy later in the course.

# **INSTRUCTIONS**
# 
# *   Set ``stop_datetime`` as the ``DataFrame`` index.
# *   Examine the index to verify that it is a ``DatetimeIndex``.
# *   Examine the ``DataFrame`` columns to confirm that ``stop_datetime`` is no longer one of the columns.

# In[22]:


ri.set_index('stop_datetime', inplace = True)


# In[23]:


ri.head()


# In[24]:


ri.index


# In[25]:


ri.columns


# In[26]:


ri.to_csv('work_area.csv', index = False)


# In[27]:


ri['drugs_related_stop'].resample('A').mean()


# In[28]:


ri.info()


# In[ ]:




