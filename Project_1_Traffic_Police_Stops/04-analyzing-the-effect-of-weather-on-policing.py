#!/usr/bin/env python
# coding: utf-8

# <h1><p style="text-align: center;">Data Analysis with Python <br>Project - 1</p><h1> - Traffic Police Stops <img src="https://docs.google.com/uc?id=17CPCwi3_VvzcS87TOsh4_U8eExOhL6Ki" class="img-fluid" width="200" height="100"> 

# In this chapter, you will use a **second dataset** to explore the impact of **weather conditions** on police behavior during traffic stops. You will practice **merging** and **reshaping** datasets, assessing whether a data source is trustworthy, working with **categorical** data, and other advanced skills.

# ## Plotting the temperature
In this exercise, you'll examine the ``temperature`` columns from the ``weather`` dataset to assess whether the data seems trustworthy. First you'll print the summary statistics, and then you'll visualize the data using a **box plot**.

When deciding whether the values seem reasonable, keep in mind that the temperature is measured in degrees **Fahrenheit**, not Celsius!
# **INSTRUCTIONS**
# 
# *   Read ``weather.csv`` into a ``DataFrame`` named ``weather``.
# *   Select the temperature columns (``TMIN``, ``TAVG``, ``TMAX``) and print their ``summary statistics`` using the ``.describe()`` method.
# *   Create a **box plot** to visualize the temperature columns.
# *   Display the plot.

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


weather = pd.read_csv('weather.csv')


# In[3]:


weather.head()


# In[4]:


weather.info()


# In[5]:


weather[['TMIN', 'TAVG', 'TMAX']].describe().transpose()


# In[6]:


plt.boxplot(weather['TAVG'].dropna(), vert = False);


# In[7]:


plt.boxplot(weather['TMIN'].dropna(), vert = False);


# In[8]:


plt.boxplot(weather['TMAX'].dropna(), vert = False);


# In[9]:


weather[['TMIN', 'TAVG', 'TMAX']].plot(kind='box')


# ***

# ## Plotting the temperature difference
In this exercise, you'll continue to assess ``whether`` the dataset seems trustworthy by plotting the difference between the maximum and minimum temperatures.

What do you notice about the resulting **histogram**? Does it match your expectations, or do you see anything unusual?
# **INSTRUCTIONS**
# 
# *   Create a new column in the ``weather`` ``DataFrame`` named ``TDIFF`` that represents the difference between the maximum and minimum temperatures.
# *   Print the summary statistics for ``TDIFF`` using the ``.describe()`` method.
# *   Create a histogram with ``20 bins`` to visualize ``TDIFF``.
# *   Display the plot.

# In[10]:


weather['TDIFF'] = weather['TMAX'] - weather['TMIN']


# In[11]:


weather[['TDIFF']].describe().transpose()


# In[12]:


weather['TDIFF'].hist(bins = 20);


# In[13]:


weather['TDIFF'].plot.hist(bins = 20)


# ***

# ## Counting bad weather conditions

# The ``weather`` ``DataFrame`` contains ``20`` columns that start with ``'WT'``, each of which represents a bad weather condition. For example:
# 
# *   ``WT05`` indicates ``"Hail"``
# *   ``WT11`` indicates ``"High or damaging winds"``
# *   ``WT17`` indicates ``"Freezing rain"``
# 
# For every row in the dataset, each ``WT`` column contains either a ``1`` (meaning the condition was present that day) or ``NaN`` (meaning the condition was not present).
# 
# In this exercise, you'll quantify ``"how bad"`` the weather was each day by counting the number of ``1`` values in each row.

# **INSTRUCTIONS**
# 
# *   Copy the columns ``WT01`` through ``WT22`` from ``weather`` to a new ``DataFrame`` named ``WT``.
# *   Calculate the sum of each row in ``WT``, and store the results in a new weather column named ``bad_conditions``.
# *   Replace any ``missing values`` in ``bad_conditions`` with a ``0``. (This has been done for you.)
# *   Create a **histogram** to visualize ``bad_conditions``, and then display the plot.

# In[14]:


WT = weather[['WT01', 'WT02',
       'WT03', 'WT04', 'WT05', 'WT06', 'WT07', 'WT08', 'WT09', 'WT10', 'WT11',
       'WT13', 'WT14', 'WT15', 'WT16', 'WT17', 'WT18', 'WT19', 'WT21', 'WT22']]


# In[15]:


WT.sum(axis = 1)


# In[16]:


weather['bad_conditions'] = WT.sum(axis = 1)


# In[17]:


weather['bad_conditions'] = weather['bad_conditions'].astype('int')


# In[18]:


weather['bad_conditions'].hist();


# In[19]:


weather['bad_conditions'].value_counts(dropna = False)


# ***

# ## Rating the weather conditions

# In the previous exercise, you counted the number of bad weather conditions each day. In this exercise, you'll use the counts to create a *rating system** for the weather.
# 
# The counts range from ``0`` to ``9``, and should be converted to ratings as follows:
# 
# *   Convert ``0`` to ``'good'``
# *   Convert ``1`` through ``4`` to ``'bad'``
# *   Convert ``5`` through ``9`` to ``'worse'``

# **INSTRUCTIONS**
# 
# *   Count the **unique** values in the ``bad_conditions`` column and sort the ``index``. 
# *   Create a ``dictionary`` called ``mapping`` that maps the ``bad_conditions`` integers to strings as specified above.
# *   Convert the ``bad_conditions`` integers to strings using the ``mapping`` and store the results in a new column called ``rating``.
# *   Count the **unique** values in ``rating`` to verify that the integers were properly converted to strings.

# In[20]:


weather['bad_conditions'].nunique()


# In[21]:


weather['bad_conditions'].sort_index()


# In[22]:


rate_system = {0 : 'good', 1 : 'bad', 2 : 'bad', 3 : 'bad', 4 : 'bad', 5 : 'worse', 6 : 'worse', 7 : 'worse',
               8 : 'worse', 9 : 'worse'}


# In[23]:


# weather['bad_conditions'] = [rate_system[item] for item in weather['bad_conditions']]


# In[24]:


weather['rating'] = weather['bad_conditions'].map(rate_system)


# In[25]:


# weather = weather.astype({'bad_conditions' : 'string'}, copy = False)


# In[26]:


# weather['rating'] = weather['bad_conditions']


# In[27]:


weather = weather.astype({'rating' : 'string'}, copy = False)


# In[28]:


del weather['bad_conditions']


# In[29]:


weather['rating'].unique()


# In[30]:


weather['rating'].value_counts()


# ***

# ## Changing the data type to category

# Since the ``rating`` column only has a few possible values, you'll change its data type to ``category`` in order to store the data more efficiently. You'll also specify a logical order for the categories, which will be useful for future exercises.

# **INSTRUCTIONS**
# 
# *   Create a ``list`` object called ``cats`` that lists the weather ratings in a logical order: ``'good'``, ``'bad'``, ``'worse'``.
# *   Change the data type of the ``rating`` column from ``object`` to ``category``. Make sure to use the ``cats list`` to define the category ordering.
# *   Examine the ``head`` of the ``rating`` column to confirm that the categories are logically ordered.

# In[31]:


cats = ['good', 'bad', 'worse']


# In[32]:


weather['rating'] = pd.Categorical(weather['rating'], categories = cats, ordered = True)


# In[33]:


weather['rating'].head()


# In[34]:


weather['rating'].min()


# In[35]:


weather['rating'].max()


# In[36]:


weather['rating'].sort_values()


# ***

# ## Preparing the DataFrames

# In this exercise, you'll prepare the **traffic stop** and **weather rating** ``DataFrames`` so that they're ready to be merged:
# 
# With the ``ri`` ``DataFrame``, you'll move the ``stop_datetime`` index to a ``column`` since the index will be lost during the merge.
# 
# With the ``weather`` ``DataFrame``, you'll select the ``DATE`` and ``rating`` columns and put them in a new ``DataFrame``.

# **INSTRUCTIONS**
# 
# * Reset the ``index`` of the ``ri`` ``DataFrame``.
# 
# * Examine the ``head`` of ``ri`` to verify that ``stop_datetime`` is now a ``DataFrame`` column, 
# and the ``index`` is now the default ``integer`` index.
# 
# * Create a new ``DataFrame`` named ``weather_rating`` that contains only the ``DATE`` and ``rating`` columns from the ``weather`` ``DataFrame``.
# 
# * Examine the ``head`` of ``weather_rating`` to verify that it contains the proper columns.

# > Before starting your work from this part of this chapter **repeat the steps which you did in the first chapter for preparing the ``ri`` data.** Continue to this chapter based on where you were in the end of the first chapter.

# In[37]:


ri = pd.read_csv('work_area.csv', low_memory = False, index_col = 0)


# In[38]:


ri.reset_index(inplace = True)


# In[39]:


ri.head()


# In[40]:


weather_rating = pd.DataFrame()


# In[41]:


weather_rating = weather[['DATE', 'rating']]


# In[42]:


weather_rating.head()


# In[43]:


weather_rating.shape


# In[44]:


ri.shape


# In[45]:


weather_rating['DATE'].nunique()


# In[46]:


ri['stop_date'].nunique()


# In[47]:


ri['stop_date']


# In[48]:


weather_rating['DATE']


# ***

# ## Merging the DataFrames

# Merging the DataFrames
# In this exercise, you'll ``merge`` the ``ri`` and ``weather_rating`` ``DataFrames`` into a new ``DataFrame``, ``ri_weather``.
# 
# The ``DataFrames`` will be joined using the ``stop_date`` column from ``ri`` and the ``DATE`` column from ``weather_rating``. Thankfully the date formatting matches exactly, which is not always the case!
# 
# Once the merge is complete, you'll set ``stop_datetime`` as the index, which is the column you saved in the previous exercise.

# Examine the shape of the ``ri`` ``DataFrame``.
# ``Merge`` the ``ri`` and ``weather_rating`` ``DataFrames`` using a ``left join``.
# Examine the ``shape`` of ``ri_weather`` to confirm that it has two more columns but the same number of rows as ``ri``.
# Replace the ``index`` of ``ri_weather`` with the ``stop_datetime`` column.

# ***

# In[49]:


ri_weather = pd.merge(ri, weather_rating, left_on = 'stop_date', right_on = 'DATE', how = 'left')


# In[50]:


ri_weather.set_index('stop_datetime', inplace = True)


# In[51]:


ri.info()


# In[52]:


ri_weather.info()


# In[53]:


ri_weather.head()


# In[54]:


weather_rating.head()


# ## Comparing arrest rates by weather rating

# Do police officers arrest drivers more often when the weather is bad? Find out below!
# 
# - **First**, you'll calculate the **overall arrest rate**.
# 
# - **Then**, you'll calculate the **arrest rate** for each of the **weather ratings** you previously assigned.
# 
# - **Finally**, you'll add **violation type** as a second factor in the analysis, to see if that accounts for any differences in the arrest rate.
# 
# Since you previously defined a logical order for the weather categories, ``good < bad < worse``, they will be sorted that way in the results.

# In[55]:


ri_weather['is_arrested'].mean()


# In[56]:


ri_weather.groupby('rating')['is_arrested'].mean()


# In[57]:


ri_weather.groupby(['violation', 'rating'])[['is_arrested']].mean()


# ***

# ## Selecting From a mult-indexed Series

# The output of a single ``.groupby()`` operation on multiple columns is a ``Series`` with a ``MultiIndex``. Working with this type of object is similar to working with a ``DataFrame``:
# 
# The ``outer`` index level is like the ``DataFrame`` rows.
# The ``inner`` index level is like the ``DataFrame`` columns.
# In this exercise, you'll practice accessing data from a multi-indexed ``Series`` using the ``.loc[]`` accessor.

# **INSTRUCTIONS**
# 
# - Save the output of the ``.groupby()`` operation from the last exercise as a new object, ``arrest_rate``.
# - Print the ``arrest_rate`` ``Series`` and examine it.
# - Print the arrest rate for ``moving violations`` in bad weather.
# - Print the arrest rates for ``speeding violations`` in all three weather conditions.

# In[58]:


arrest_rate = ri_weather.groupby(['violation', 'rating'])['is_arrested'].mean()


# In[59]:


arrest_rate


# In[60]:


arrest_rate.loc['Moving violation']['bad']


# In[61]:


arrest_rate['Speeding']


# In[62]:


arrest_rate['Moving violation']['bad']


# ***

# ## Reshaping the arrest rate data

# In this exercise, you'll start by **reshaping** the ``arrest_rate`` ``Series`` into a ``DataFrame``. This is a useful step when working with any multi-indexed ``Series``, since it enables you to access the full range of ``DataFrame`` methods.
# 
# Then, you'll create the exact same ``DataFrame`` using a ``pivot table``. This is a great example of how pandas often gives you more than one way to reach the same result!

# **INSTRUCTIONS**
# 
# - ``unstack`` the ``arrest_rate`` ``Series`` to ``reshape`` it into a ``DataFrame``.
# - Create the exact same ``DataFrame`` using a ``pivot table``! Each of the three ``.pivot_table()`` parameters should be specified as one of the ``ri_weather`` columns.

# In[64]:


arrest_rate


# In[65]:


arrest_rate.unstack()


# In[67]:


ri_weather.groupby(['violation', 'rating'])['is_arrested'].mean()


# In[68]:


arrest_rate2 = ri_weather.pivot_table(values = 'is_arrested', index = 'violation', columns = 'rating')
# default aggfunc is mean.


# In[69]:


arrest_rate2

