#!/usr/bin/env python
# coding: utf-8

# <h1><p style="text-align: center;">Data Analysis with Python <br>Project - 1</p><h1> - Traffic Police Stops <img src="https://docs.google.com/uc?id=17CPCwi3_VvzcS87TOsh4_U8eExOhL6Ki" class="img-fluid" width="200" height="100"> 

# Does the ``gender`` of a driver have an impact on police behavior during a traffic stop? **In this chapter**, you will explore that question while practicing filtering, grouping, method chaining, Boolean math, string methods, and more!

# ***

# ## Examining traffic violations

# Before comparing the violations being committed by each gender, you should examine the ``violations`` committed by all drivers to get a baseline understanding of the data.
# 
# In this exercise, you'll count the unique values in the ``violation`` column, and then separately express those counts as proportions.

# > Before starting your work in this section **repeat the steps which you did in the previos chapter for preparing the data.** Continue to this chapter based on where you were in the end of the previous chapter.

# In[1]:


import pandas as pd


# In[2]:


ri = pd.read_csv('work_area.csv', low_memory = False, index_col = 0)


# In[3]:


ri.head()


# **INSTRUCTIONS**
# 
# *   Count the unique values in the ``violation`` column, to see what violations are being committed by all drivers.
# *   Express the violation counts as proportions of the total.

# In[4]:


ri.columns


# In[5]:


ri.info()


# In[6]:


ri[['violation']].nunique()


# In[7]:


ri[['violation']].value_counts().sum()


# In[8]:


ri[['violation']].value_counts()


# In[9]:


ri[['violation']].value_counts() / ri[['violation']].value_counts().sum()
# ri['violation'].value_counts(normalize = True)


# In[10]:


ri['violation'].value_counts(normalize = True)


# ***

# ## Comparing violations by gender

# The question we're trying to answer is whether male and female drivers tend to commit different types of traffic violations.
# 
# You'll first create a ``DataFrame`` for each gender, and then analyze the ``violations`` in each ``DataFrame`` separately.

# **INSTRUCTIONS**
# 
# *   Create a ``DataFrame``, female, that only contains rows in which ``driver_gender`` is ``'F'``.
# *   Create a ``DataFrame``, male, that only contains rows in which ``driver_gender`` is ``'M'``.
# *   Count the ``violations`` committed by female drivers and express them as proportions.
# *   Count the violations committed by male drivers and express them as proportions.

# In[11]:


ri_female = ri[ri['driver_gender'] == 'F']


# In[12]:


ri_male = ri[ri['driver_gender'] == 'M']


# In[13]:


ri_female[['violation']].value_counts()


# In[14]:


ri_female[['violation']].value_counts().sum()


# In[15]:


# ri_female[['violation']].value_counts() / ri_female[['violation']].value_counts().sum()
ri_female[['violation']].value_counts(normalize = True)


# In[16]:


ri_male[['violation']].value_counts()


# In[17]:


ri_male[['violation']].value_counts().sum()


# In[18]:


# ri_male[['violation']].value_counts() / ri_male[['violation']].value_counts().sum()
ri_male[['violation']].value_counts(normalize = True)


# ***

# ## Comparing speeding outcomes by gender

# When a driver is pulled over for speeding, many people believe that gender has an impact on whether the driver will receive a ticket or a warning. Can you find evidence of this in the dataset?
# 
# First, you'll create two ``DataFrames`` of drivers who were stopped for ``speeding``: one containing ***females*** and the other containing ***males***.
# 
# Then, for each **gender**, you'll use the ``stop_outcome`` column to calculate what percentage of stops resulted in a ``"Citation"`` (meaning a ticket) versus a ``"Warning"``.

# **INSTRUCTIONS**
# 
# *   Create a ``DataFrame``, ``female_and_speeding``, that only includes female drivers who were stopped for speeding.
# *   Create a ``DataFrame``, ``male_and_speeding``, that only includes male drivers who were stopped for speeding.
# *   Count the **stop outcomes** for the female drivers and express them as proportions.
# *   Count the **stop outcomes** for the male drivers and express them as proportions.

# In[19]:


female_and_speeding = ri_female[ri_female['violation'] == 'Speeding']


# In[20]:


male_and_speeding = ri_male[ri_male['violation'] == 'Speeding']


# In[21]:


female_and_speeding[['stop_outcome']].value_counts()


# In[22]:


female_and_speeding[['stop_outcome']].value_counts().sum()


# In[23]:


# female_and_speeding[['stop_outcome']].value_counts() / female_and_speeding[['stop_outcome']].value_counts().sum()
female_and_speeding[['stop_outcome']].value_counts(normalize = True) 


# In[24]:


f = female_and_speeding[['stop_outcome']].value_counts() / female_and_speeding[['stop_outcome']].value_counts().sum()


# In[25]:


male_and_speeding[['stop_outcome']].value_counts()


# In[26]:


male_and_speeding[['stop_outcome']].value_counts().sum()


# In[27]:


male_and_speeding[['stop_outcome']].value_counts() / male_and_speeding[['stop_outcome']].value_counts().sum()


# In[28]:


m = male_and_speeding[['stop_outcome']].value_counts() / male_and_speeding[['stop_outcome']].value_counts().sum()


# In[29]:


f['Citation']


# In[30]:


f['Warning']


# In[31]:


m['Citation']


# In[32]:


m['Warning']


# ***

# ## Calculating the search rate

# During a traffic stop, the police officer sometimes conducts a search of the vehicle. In this exercise, you'll calculate the percentage of all stops that result in a vehicle search, also known as the **search rate**.

# **INSTRUCTIONS**
# 
# *   Check the data type of ``search_conducted`` to confirm that it's a ``Boolean Series``.
# *   Calculate the search rate by counting the ``Series`` values and expressing them as proportions.
# *   Calculate the search rate by taking the mean of the ``Series``. (It should match the proportion of ``True`` values calculated above.)

# In[33]:


ri['search_conducted'].dtype


# In[34]:


ri['search_conducted'].value_counts()


# In[35]:


ri['search_conducted'].value_counts() / ri['search_conducted'].value_counts().sum()


# In[36]:


ri['search_conducted'].mean()


# ***

# ## Comparing search rates by gender

# You'll compare the rates at which **female** and **male** drivers are searched during a traffic stop. Remember that the vehicle search rate across all stops is about **3.8%**.
# 
# First, you'll filter the ``DataFrame`` by gender and calculate the search rate for each group separately. Then, you'll perform the same calculation for both genders at once using a ``.groupby()``.

# **INSTRUCTIONS 1/3**
# 
# *   Filter the ``DataFrame`` to only include **female** drivers, and then calculate the search rate by taking the mean of ``search_conducted``.

# In[37]:


ri[ri['driver_gender'] == 'F']['search_conducted'].mean()


# **INSTRUCTIONS 2/3**
# 
# *   Filter the ``DataFrame`` to only include **male** drivers, and then repeat the search rate calculation.

# In[38]:


ri[ri['driver_gender'] == 'M']['search_conducted'].mean()


# **INSTRUCTIONS 3/3**
# 
# *   Group by driver gender to calculate the search rate for both groups simultaneously. (It should match the previous results.)

# In[39]:


ri.groupby(['driver_gender']).mean()['search_conducted']


# ***

# ## Adding a second factor to the analysis

# Even though the search rate for males is much higher than for females, it's possible that the difference is mostly due to a second factor.
# 
# For example, you might hypothesize that the search rate varies by violation type, and the difference in search rate between males and females is because they tend to commit different violations.
# 
# You can test this hypothesis by examining the search rate for each combination of gender and violation. If the hypothesis was true, you would find that males and females are searched at about the same rate for each violation. Find out below if that's the case!

# **INSTRUCTIONS 1/2**
# 
# *   Use a ``.groupby()`` to calculate the search rate for each combination of gender and violation. Are males and females searched at about the same rate for each violation?

# In[40]:


ri.groupby(['driver_gender', 'violation']).mean()[['search_conducted']]


# **INSTRUCTIONS 2/2**
# 
# *   Reverse the ordering to group by violation before gender. The results may be easier to compare when presented this way.

# In[41]:


ri.groupby(['violation', 'driver_gender']).mean('search_conducted')[['search_conducted']]


# ***

# ## Counting protective frisks

# During a vehicle search, the police officer may pat down the driver to check if they have a weapon. This is known as a ``"protective frisk."``
# 
# You'll first check to see how many times "Protective Frisk" was the only search type. Then, you'll use a string method to locate all instances in which the driver was frisked.

# **INSTRUCTIONS**
# 
# *   Count the ``search_type`` values to see how many times ``"Protective Frisk"`` was the only search type.
# *   Create a new column, frisk, that is ``True`` if ``search_type`` contains the string ``"Protective Frisk"`` and ``False`` otherwise.
# *   Check the data type of frisk to confirm that it's a ``Boolean Series``.
# *   Take the sum of frisk to count the total number of frisks.

# In[42]:


ri['search_type'].str.contains('Protective Frisk').value_counts()


# In[43]:


ri['frisk'] = ri['search_type'].str.contains('Protective Frisk', na = False)


# In[44]:


ri['frisk']


# In[45]:


ri['frisk'].dtype


# In[46]:


ri['frisk'].sum()


# ***

# ## Comparing frisk rates by gender

# You'll compare the rates at which female and male drivers are frisked during a search. Are males frisked more often than females, perhaps because police officers consider them to be higher risk?
# 
# Before doing any calculations, it's important to filter the ``DataFrame`` to only include the relevant subset of data, namely stops in which a search was conducted.

# **INSTRUCTIONS**
# 
# *   Create a ``DataFrame``, searched, that only contains rows in which ``search_conducted`` is ``True``.
# *   Take the mean of the frisk column to find out what percentage of searches included a frisk.
# *   Calculate the frisk rate for each gender using a ``.groupby()``.

# In[47]:


ri_search = ri[ri['search_conducted'] == True]


# In[48]:


ri_search['frisk'].mean()


# In[49]:


ri_search.groupby(['driver_gender']).mean()[['frisk']]

