#!/usr/bin/env python
# coding: utf-8

# <h1><p style="text-align: center;">Data Analysis with Python <br>Project - 1</p><h1> - Traffic Police Stops <img src="https://docs.google.com/uc?id=17CPCwi3_VvzcS87TOsh4_U8eExOhL6Ki" class="img-fluid" " width="200" height="100"> 

# Are you more likely to get arrested at a certain time of day? Are drug-related stops on the rise? In this chapter, you will answer these and other questions by analyzing the dataset visually, since plots can help you to understand trends in a way that examining the raw data cannot.

# ## Calculating the hourly arrest rate

# When a police officer stops a driver, a small percentage of those stops ends in an arrest. This is known as the **arrest rate**. In this exercise, you'll find out whether the arrest rate varies by time of day.
# 
# First, you'll calculate the arrest rate across all stops. Then, you'll calculate the **hourly arrest rate** by using the ``hour`` attribute of the ``index``. The hour ranges from ``0`` to ``23``, in which:
# 
# ``0 = midnight``<br>
# ``12 = noon`` <br>
# ``23 = 11 PM``

# > Before starting your work in this section **repeat the steps which you did in the first chapter for preparing the data.** Continue to this chapter based on where you were in the end of the first chapter.

# **INSTRUCTIONS**
# 
# *   Take the mean of the ``is_arrested`` column to calculate the overall arrest rate.
# *   Group by the ``hour`` attribute of the ``DataFrame`` index to calculate the hourly arrest rate.
# *   Save the **hourly arrest rate** ``Series`` as a new object, ``hourly_arrest_rate``.

# In[1]:


import pandas as pd


# In[2]:


ri = pd.read_csv('work_area.csv', low_memory = False, index_col = 0)


# In[3]:


ri.head()


# In[4]:


ri['is_arrested'].mean()


# In[5]:


ri.groupby(pd.to_datetime(ri['stop_time'], format = '%H:%M').dt.hour)[['is_arrested']].mean()


# In[6]:


hourly_arrest_rate = ri.groupby(pd.to_datetime(ri['stop_time'], format = '%H:%M').dt.hour)['is_arrested'].mean()


# In[7]:


ri.index = pd.to_datetime(ri.index)


# In[8]:


ri.index.hour


# In[9]:


ri.groupby(ri.index.hour)[['is_arrested']].mean()


# In[10]:


# hourly_arrest_rate = ri.groupby(ri.index.hour)[['is_arrested']].mean()


# ***

# ## Plotting the hourly arrest rate

# You'll create a line plot from the ``hourly_arrest_rate`` object. A line plot is appropriate in this case because you're showing how a quantity changes over time.
# 
# This plot should help you to spot some trends that may not have been obvious when examining the raw numbers!

# **INSTRUCTIONS**
# 
# *   Import ``matplotlib.pyplot`` using the alias ``plt``.
# *   Create a **line plot** of ``hourly_arrest_rate`` using the ``.plot()`` method.
# *   Label the ``x-axis`` as ``'Hour'``, label the ``y-axis`` as ``'Arrest Rate'``, and title the plot ``'Arrest Rate by Time of Day'``.
# *   Display the plot using the ``.show()`` function.

# In[11]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[12]:


sns.set(style="darkgrid")
hourly_arrest_rate.plot()
# plt.plot(hourly_arrest_rate)
plt.xlabel('Hour')
plt.ylabel('Arrest Rate')
plt.title('Arrest Rate by Time of Day')
plt.show()


# ***

# ## Plotting drug-related stops

# In a small portion of traffic stops, drugs are found in the vehicle during a search. You'll assess whether these **drug-related stops** are becoming more common over time.
# 
# The Boolean column ``drugs_related_stop`` indicates whether drugs were found during a given stop. You'll calculate the **annual drug rate** by **resampling** this column, and then you'll use a line plot to visualize how the rate has changed over time.

# **INSTRUCTIONS**
# 
# *   Calculate the **annual rate** of drug-related stops by **resampling** the ``drugs_related_stop`` column (on the ``'A'`` frequency) and taking the mean.
# *   Save the annual drug rate ``Series`` as a new object, ``annual_drug_rate``.
# *   Create a line plot of ``annual_drug_rate`` using the ``.plot()`` method.
# *   Display the plot using the ``.show()`` function.

# In[13]:


ri['drugs_related_stop'].resample('A').mean()  # A = Annually


# In[14]:


ri['drugs_related_stop'].resample('Q').mean()


# In[15]:


annual_drug_rate = ri['drugs_related_stop'].resample('A').mean()


# In[16]:


annual_drug_rate.plot()
plt.show()


# ## Comparing drug and search rates (to be deleted)

# As you saw in the last exercise, the rate of **drug-related stops** increased significantly between ``2005`` and ``2015``. You might hypothesize that the rate of vehicle searches was also increasing, which would have led to an increase in drug-related stops even if more drivers were not carrying drugs.
# 
# You can test this hypothesis by calculating the annual search rate, and then plotting it against the annual drug rate. If the hypothesis is true, then you'll see both rates increasing over time.

# **INSTRUCTIONS**
# 
# *   Calculate the annual search rate by **resampling** the ``search_conducted`` column, and save the result as ``annual_search_rate``.
# *   Concatenate ``annual_drug_rate`` and ``annual_search_rate`` along the ``columns axis``, and save the result as ``annual``.
# *   Create subplots of the drug and search rates from the ``annual`` ``DataFrame``.
# *   Display the subplots.

# In[17]:


annual_search_rate = ri['search_conducted'].resample('A').mean()


# In[18]:


df1 = pd.DataFrame(annual_search_rate)


# In[19]:


df2 = pd.DataFrame(annual_drug_rate)


# In[20]:


annual = pd.concat([df1, df2], axis = 1)


# In[21]:


annual


# In[22]:


fig, axes = plt.subplots(nrows=2, ncols=1, figsize = (8, 6))

annual['search_conducted'].plot(ax=axes[0])
annual['drugs_related_stop'].plot(ax=axes[1])
plt.tight_layout()


# In[23]:


annual.plot(subplots = True, figsize = (10, 8))
plt.show()


# ***

# ## Tallying violations by district

# The state of **Rhode Island** is broken into six police districts, also known as zones. How do the zones compare in terms of what violations are caught by police?
# 
# In this exercise, you'll create a frequency table to determine how many violations of each type took place in each of the six zones. Then, you'll filter the table to focus on the ``"K"`` zones, which you'll examine further in the next exercise.

# **INSTRUCTIONS**
# 
# *   Create a ``frequency table`` from the ``district`` and ``violation`` columns using the ``pd.crosstab()`` function.
# *   Save the ``frequency table`` as a new object, ``all_zones``.
# *   Select rows ``'Zone K1'`` through ``'Zone K3'`` from ``all_zones`` using the ``.loc[]`` accessor.
# *   Save the smaller table as a new object, ``k_zones``.

# In[24]:


pd.crosstab(ri['district'], ri['violation'])


# In[25]:


all_zones = pd.crosstab(ri.district, [ri['violation']])


# In[26]:


all_zones.loc['Zone K1' : 'Zone K3']


# In[27]:


k_zones = all_zones.loc['Zone K1' : 'Zone K3']


# ***

# ## Plotting violations by district

# Now that you've created a frequency table focused on the ``"K"`` zones, you'll visualize the data to help you compare what violations are being caught in each zone.
# 
# First you'll create a **bar plot**, which is an appropriate plot type since you're comparing categorical data. Then you'll create a **stacked bar plot** in order to get a slightly different look at the data. Which plot do you find to be more insightful?

# **INSTRUCTIONS 1/2**
# 
# *   Create a bar plot of ``k_zones``.
# *   Display the plot and examine it. What do you notice about each of the zones?

# In[28]:


k_zones.plot.bar(figsize = (10, 6))
plt.show()


#   Numbers of violations of each zone have relatively rate. Probably, Zone K3 is more crowded than K2 and
# K2 is more crowded than K1.

# **INSTRUCTIONS 2/2**
# 
# *   Create a stacked bar plot of ``k_zones``.
# *   Display the plot and examine it. Do you notice anything different about the data than you did previously?

# In[29]:


k_zones.plot.bar(stacked = True);


#   There are more violations at K3 than others and there are more vioalations at K2 than K1.

# ***

# ## Converting stop durations to numbers

# In the traffic stops dataset, the ``stop_duration`` column tells you approximately how long the driver was detained by the officer. Unfortunately, the durations are stored as ``strings``, such as ``'0-15 Min'``. How can you make this data easier to analyze?
# 
# In this exercise, you'll convert the **stop durations** to ``integers``. Because the precise durations are not available, you'll have to estimate the numbers using reasonable values:
# 
# *   Convert ``'0-15 Min'`` to ``8``
# *   Convert ``'16-30 Min'`` to ``23``
# *   Convert ``'30+ Min'`` to ``45``

# **INSTRUCTIONS**
# 
# *   Print the **unique values** in the ``stop_duration`` column. (This has been done for you.)
# *   Create a ``dictionary`` called ``mapping`` that maps the ``stop_duration`` strings to the integers specified above.
# *   Convert the ``stop_duration`` strings to integers using the ``mapping``, and store the results in a new column called ``stop_minutes``.
# *   Print the unique values in the ``stop_minutes`` column, to verify that the durations were properly converted to integers.

# In[30]:


ri['stop_duration'].unique()


# In[31]:


durations = {'0-15 Min' : 8, '16-30 Min' : 23, '30+ Min' : 45}


# In[32]:


ri['stop_minutes'] = ri['stop_duration'].map(durations)


# In[33]:


ri['stop_minutes'].value_counts(dropna = False)


# In[34]:


durations2 = {'0-15 Min' : 8, '16-30 Min' : 23, '30+ Min' : 45, '2' : 120, '1' : 60}


# In[35]:


ri['stop_minutes2'] = [durations2[item] for item in ri['stop_duration']]


# In[36]:


ri['stop_minutes2'].value_counts(dropna = False)


# ***

# ## Plotting stop length
If you were stopped for a particular violation, how long might you expect to be detained?

In this exercise, you'll visualize the **average length** of time drivers are stopped for each **type** of **violation**. Rather than using the ``violation`` column in this exercise, you'll use ``violation_raw`` since it contains more detailed descriptions of the violations.
# **INSTRUCTIONS**
# 
# *   For each value in the ``violation_raw`` column, calculate the **mean number** of ``stop_minutes`` that a driver is detained.
# *   Save the resulting ``Series`` as a new object, ``stop_length``.
# *   Sort ``stop_length`` by its values, and then visualize it using a **horizontal bar plot**.
# *   Display the plot.

# In[37]:


ri.groupby('violation_raw').mean()['stop_minutes']


# In[38]:


stop_lenght = ri.groupby('violation_raw').mean()['stop_minutes']


# In[39]:


stop_lenght.sort_values()


# In[40]:


stop_lenght.sort_values().plot.barh();

