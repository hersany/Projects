#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import numpy as np 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter
import warnings
warnings.filterwarnings('ignore') 


# INSTRUCTIONS
# 1. Mean poverty rate of each state
# 1. Most common 15 Name or Surname of killed people
# 1. Killed People According to Races
# 1. Box and Swarm Plots in kill data
# 1. Kill properties (Count Plot)
#     * Number of people by gender
#     * Kill weapon
#     * Age of killed people
#     * Race of killed people
#     * Most dangerous cities
#     * Most dangerous states
#     * Having mental ilness or not for killed people
#     * Threat types
#     * Flee types
# <br>

# In[2]:


pr = pd.read_csv('PercentagePeopleBelowPovertyLevel.csv', encoding="windows-1252")
sr = pd.read_csv('ShareRaceByCity.csv', encoding="windows-1252")
kill = pd.read_csv('PoliceKillingsUS.csv', encoding="windows-1252")


# ## 1. Mean poverty rate of each state

# In[3]:


pr.info()


# In[4]:


pr.head()

Problem: We don't know what does "-" mean. We need to clean it. Maybe we can consider it as 0.
# **INSTRUCTION-1: replace the "-" with zero.**

# In[3]:


pr['poverty_rate'].replace('-', 0, inplace = True)


# In[4]:


pr['poverty_rate'].value_counts()


# In[5]:


pr.info()

Problem: data type of poverty_rate colum is object. We need to convert it to a numeric type (float).
# **INSTRUCTION-2 : Convert type of poverty_rate colum to a numeric type (float).**

# In[6]:


pr['poverty_rate'] = pd.to_numeric(pr['poverty_rate'])


# **INSTRUCTION-3 : Plot the Poverty rate of each state. (Demonstrate mean value of each Geogrophic Area (AL, AK, AR).)**

# **INSTRUCTION-3.a.1 : Plot With Pandas Built in method:**

# In[7]:


pr.groupby('Geographic Area')[['poverty_rate']].mean()


# In[10]:


pr.groupby('Geographic Area')[['poverty_rate']].mean().plot.bar(figsize = (15, 10))
plt.xlabel('States', fontsize = 15)
plt.ylabel('Poverty Rate', fontsize = 15)
plt.title('Poverty Rate Given States', fontsize = 18)
plt.xticks(rotation = 45)
plt.show()


# **INSTRUCTION-3.a.2 : Plot Sorted Values With Pandas Built in method:**

# In[11]:


pr.head()


# In[13]:


pr.groupby('Geographic Area')['poverty_rate'].mean().sort_values(ascending = False).plot.bar(figsize = (15, 10))
plt.xlabel('States', fontsize = 15)
plt.ylabel('Poverty Rate', fontsize = 15)
plt.title('Poverty Rate Given States', fontsize = 15)
plt.xticks(rotation = 45)
plt.show()


# **INSTRUCTION-3.b : Plot Sorted Values With Matplotlib:** 

# In[16]:


a = pr.groupby('Geographic Area')[['poverty_rate']].mean().sort_values(by = 'poverty_rate',                                          ascending = False)['poverty_rate'].values


# In[14]:


b = pr.groupby('Geographic Area')[['poverty_rate']].mean().sort_values(by = 'poverty_rate',                                           ascending = False).index


# In[15]:


plt.figure(figsize = (15, 10))
plt.bar(b, a)
plt.xlabel('States', fontsize = 15)
plt.ylabel('Poverty Rate', fontsize = 15)
plt.title('Poverty Rate Given States', fontsize = 15)
plt.xticks(rotation = 45)
plt.show()


# **INSTRUCTION-3.c : Plot Sorted Values With Seaborn** 

# In[16]:


pr.info()


# In[55]:


pr.groupby('Geographic Area')[['poverty_rate']].mean().sort_values('poverty_rate', ascending = False).index


# In[18]:


plt.figure(figsize = (15, 10))
sns.barplot(b, a)
plt.xlabel('States', fontsize = 15)
plt.ylabel('Poverty Rate', fontsize = 15)
plt.title('Poverty Rate Given States', fontsize = 15)
plt.xticks(rotation = 45)
plt.show()


# In[54]:


plt.figure(figsize = (15, 10))
sns.barplot(x = 'Geographic Area', y = 'poverty_rate', data = pr, ci = None, order = pr.groupby('Geographic Area')[['poverty_rate']].mean().sort_values('poverty_rate', ascending = False).index)
plt.xlabel('States', fontsize = 15)
plt.ylabel('Poverty Rate', fontsize = 15)
plt.title('Poverty Rate Given States', fontsize = 15)
plt.xticks(rotation = 45)
plt.show()


# ## 2. Most common 15 Name or Surname of killed people 

# In[20]:


kill.head()


# In[21]:


kill.name.value_counts()


# In[8]:


# Problem: TK TK is most probably not a name or surname. We will clean them.
pairs = kill.name[kill.name != 'TK TK'].str.split()
pairs.head()


# **INSTRUCTION : Plot Most common 15 Name or Surname of killed people** 
# Clue 1: You need to separate the names and surnames because we are asking most common name OR surname.

# Clue 2 :After seperation make a whole list that contains both names and surnames.

# Clue 3 : How to separate the name and surname pairs?

>>> pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
>>> numbers, letters = zip(*pairs)
>>> numbers
(1, 2, 3, 4)
>>> letters
('a', 'b', 'c', 'd')

# Clue 4: You can use Counter() and most_common() built in functions together to find the most common names or surnames, or you can write your functions for this purpose.
# In[9]:


pairs = pairs.apply(','.join)


# In[10]:


pairs = pd.DataFrame(pairs)


# In[11]:


pairs2 = pairs['name'].str.get_dummies(',')


# In[12]:


pairs2.head(2)


# In[13]:


pairs2.shape


# In[14]:


pairs2.sum(axis = 0).sort_values(ascending = False).head(15)


# In[15]:


a = pairs2.sum(axis = 0).sort_values(ascending = False).head(15).index


# In[16]:


b = pairs2.sum(axis = 0).sort_values(ascending = False).head(15).values


# In[17]:


plt.figure(figsize = (15, 10))
g = sns.barplot(a, b)
plt.title('Most common 15 Name or Surname of killed people')
plt.xlabel('Name or Surname of killed people')
plt.ylabel('Frequency')
plt.xticks(rotation = 45)
for p in g.patches:
    g.annotate((p.get_height()), (p.get_x()+0.2, p.get_height()+0.6))
plt.show()


# In[69]:


# Problem: TK TK is most probably not a name or surname. We will clean them.
pairs = kill.name[kill.name != 'TK TK'].str.split()
pairs.head()


# In[70]:


df = pd.DataFrame(pairs)


# In[71]:


df.head(2)


# In[72]:


df['len'] = df['name'].apply(len)


# In[73]:


df.head(2)


# In[74]:


df['len'].value_counts()


# In[75]:


two_names = df.name[df.len == 2]


# In[76]:


two_names.head(2)


# In[77]:


three_names = df.name[df.len == 3]


# In[78]:


four_names = df.name[df.len == 4]


# In[79]:


a, b = zip(*two_names)


# In[80]:


a[:5]


# In[81]:


b[:5]


# In[82]:


c, d, e = zip(*three_names)


# In[83]:


f, g, h, j = zip(*four_names)


# In[84]:


total_list = a+b+c+d+e+f+g+h+j


# In[85]:


len(total_list)


# In[86]:


Counter(total_list)


# In[87]:


name_count = Counter(total_list)


# In[88]:


most_common_names = name_count.most_common(15)


# In[89]:


most_common_names


# In[90]:


x, y = zip(*most_common_names)


# In[93]:


x, y = list(x), list(y)


# In[94]:


plt.figure(figsize = (15, 10))
sns.barplot(x, y)
plt.title('Most common 15 Name or Surname of killed people')
plt.xlabel('Name or Surname of killed people')
plt.ylabel('Frequency')
plt.xticks(rotation = 45)
plt.show()


# ## 3. Killed People According to Races (Pie Chart)

# In[29]:


kill.head()


# In[30]:


kill.race.unique()


# In[31]:


kill.race.value_counts()


# In[32]:


sr.head(2)


# In[33]:


kill.info()


# Problem: missing value on race column.

# **INSTRUCTION-1: Drop the all raws that contain missing value (dropna)**

# In[34]:


kill.dropna(subset = ['race'], inplace = True)


# In[35]:


kill.info()


# **INSTRUCTION-2: Demonstrate Race Ratio of Killed People by a Pie Chart**

# In[36]:


plt.figure(figsize = (15, 10))
plt.pie(kill['race'].value_counts(),labels = kill['race'].value_counts().index, autopct='%1.1f%%')
plt.title('Killed People According to Races', fontsize = 15, color = 'blue')
plt.show()


# In[38]:


plt.figure(figsize = (15, 10))
kill['race'].value_counts().plot.pie(autopct='%1.1f%%')
plt.title('Killed People According to Races', fontsize = 15, color = 'blue')
plt.show()


# ## 4a.Box plot of age in both genders separeted by manner of death.

# In[37]:


kill.head()


# In[38]:


kill.manner_of_death.unique()


# **INSTRUCTION: Demonstrate the Qurtiles of age in both genders separeted by manner of death.**

# In[39]:


kill['manner_of_death'].value_counts(dropna = False).plot.box()


# In[40]:


sns.boxplot(kill['manner_of_death'].value_counts(dropna = False))


# In[41]:


kill.head(2)


# In[95]:


plt.figure(figsize = (10, 7))
sns.boxplot('gender', 'age', 'manner_of_death', kill)


# In[98]:


plt.figure(figsize = (10, 7))
sns.violinplot('gender', 'age', 'manner_of_death', kill)


# In[97]:


plt.figure(figsize = (10, 7))
sns.swarmplot('gender', 'age', 'manner_of_death', kill, dodge = True)


# ## 4b. Swarm Plot (Do not use in large datasets. The memory will not be enogh!)

# **INSTRUCTION: Demonstrate the age in both genders separeted by manner of death by a swarm plot.**

# In[98]:


plt.figure(figsize = (10, 7))
sns.swarmplot('gender', 'age', 'manner_of_death', kill)


# ## 5. Kill properties (Count Plots)

# **INSTRUCTION-1: Plot number of poeple by gender**

# In[49]:


sns.countplot('gender', data = kill)


# **INSTRUCTION-2: Plot 7 most common kill weapons**

# In[113]:


plt.figure(figsize = (10, 6))
sns.countplot('armed', data = kill, order = kill['armed'].value_counts().iloc[:7].index)
plt.title('Kill weapon', fontsize = 15, color = 'blue')
plt.xlabel('Weapon Types', fontsize = 12)
plt.ylabel('Number of Weapon', fontsize = 12)
plt.show()


# In[112]:


plt.figure(figsize = (10, 6))
sns.countplot('armed', data = kill, order = kill['armed'].value_counts().index[0:7])
plt.title('Kill weapon', fontsize = 15, color = 'blue')
plt.xlabel('Weapon Types', fontsize = 12)
plt.ylabel('Number of Weapon', fontsize = 12)
plt.show()


# **INSTRUCTION-3: Plot number of age of killed people under two groups : Under 25 and Above 25**

# In[58]:


kill.head(2)


# In[99]:


kill['age_cat'] = kill['age'].apply(lambda x : 'Above 25' if x >= 25 else 'Under 25')


# In[100]:


sns.countplot('age_cat', data = kill)


# In[70]:


kill[kill['age'] < 25].count()['id']


# In[71]:


kill[kill['age'] > 25].count()['id']


# In[72]:


kill[kill['age'] == 25].count()['id']


# In[63]:


sns.countplot('signs_of_mental_illness', data = kill[kill['age'] < 25])
sns.countplot('signs_of_mental_illness', data = kill[kill['age'] > 25])


# In[60]:


kill.groupby('age')['id'].count()


# **INSTRUCTION-4: Plot number of killed poeple by race**

# In[71]:


sns.countplot('race', data = kill)
plt.show()


# **INSTRUCTION-5: Plot 12 most dangerous cities**

# In[80]:


plt.figure(figsize = (10, 7))
sns.countplot('city', data = kill, order = kill['city'].value_counts().iloc[:12].index)
plt.title('Most dangerous cities', fontsize = 12, color = 'blue')
plt.xticks(rotation = 45)
plt.show()


# **INSTRUCTION-6: Plot 20 most dangerous states**

# In[101]:


plt.figure(figsize = (10, 7))
sns.countplot('state', data = kill, order = kill['state'].value_counts().iloc[:20].index)
plt.title('Most dangerous states', fontsize = 12, color = 'blue')
plt.show()


# **INSTRUCTION-7: Plot Having mental ilness or not for killed people**

# In[93]:


plt.figure(figsize = (8, 5))
sns.countplot('signs_of_mental_illness', data = kill)
plt.xlabel('Mental ilness')
plt.ylabel('Number ofMental İllness')
plt.title('Having mental illness or not', fontsize = 15, color = 'blue')
plt.show()


# **INSTRUCTION-8: Plot number of Threat Types**

# In[92]:


plt.figure(figsize = (8, 5))
sns.countplot('threat_level', data = kill)
plt.xlabel('Threat types')
plt.ylabel('Frequency')
plt.title('Threat types', fontsize = 15, color = 'blue')
plt.show()


# **INSTRUCTION-9: Plot number of Flee Types**

# In[95]:


plt.figure(figsize = (8, 5))
sns.countplot('flee', data = kill)
plt.xlabel('Flee types')
plt.ylabel('Frequency')
plt.title('Flee types', fontsize = 15, color = 'blue')
plt.show()

