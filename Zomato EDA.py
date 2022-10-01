#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Imported importance dictionary

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


# Import both the files in to the jupiter

df1 = pd.read_excel("C:\\EDA\\1. Training\\Python\\Zomato\\zomato.xlsx")
df2 = pd.read_excel("C:\\EDA\\1. Training\\Python\\Zomato\\Country-Code.xlsx")


# In[3]:


# Check latest observations from df1

df1.head()


# In[4]:


# Check latest observations from df2

df2.head()


# In[5]:


# Checking no of Raw and column
df1.shape


# In[6]:


# Checking no of Raw and column
df2.shape


# In[7]:


# using left join in df1 from df2 and add country column in df1 
df1 = pd.merge(df1, df2,  on ='Country Code', how ='left')
df1.head(2)


# # Data Dictionary 
# • Restaurant Id: Unique id of every restaurant across various cities of the world
# • Restaurant Name: Name of the restaurant
# • Country Code: Country in which restaurant is located
# • City: City in which restaurant is located
# • Address: Address of the restaurant
# • Locality: Location in the city
# • Locality Verbose: Detailed description of the locality
# • Longitude: Longitude coordinate of the restaurant’s location
# • Latitude: Latitude coordinate of the restaurant’s location
# • Cuisines: Cuisines offered by the restaurant
# • Average Cost for two: Cost for two people in different currencies 👫
# • Currency: Currency of the country
# • Has Table booking: yes/no
# • Has Online delivery: yes/ no
# • Is delivering: yes/ no
# • Switch to order menu: yes/no
# • Price range: range of price of food
# • Aggregate Rating: Average rating out of 5
# • Rating color: depending upon the average rating color
# • Rating text: text-based on the rating of rating
# • Votes: Number of ratings cast by people

# In[8]:


# Country column is added now. We have 22 columns
df1.shape


# In[9]:


# No changes in the df2

df2.head(3)


# In[10]:


df1.isnull().sum()

# There is 9 null values in Cuisines


# In[11]:


#There is no duplicated values in our data

df1.duplicated().sum()


# # Replace blank value in the Cuisines with the help of Mode

# In[12]:


df1['Cuisines'] = df1['Cuisines'].fillna(df1['Cuisines'].mode()[0])


# In[13]:


df1.isnull().sum()


# In[14]:


# Knowing the datatypes which we are exploring
df1.dtypes


# In[15]:


df1


# # Unique values in the data

# In[16]:


df1['Has Table booking'].unique()


# In[17]:


df1['Is delivering now'].unique()


# In[18]:


df1['Switch to order menu'].unique()


# In[19]:


df1['Has Online delivery'].unique()


# In[20]:


df1['Rating color'].unique()


# # Visualize the Unique counts

# In[21]:


df1.dtypes


# In[22]:


sns.countplot(df1['Has Table booking'])

# Maximum no of customeres are not booking table in advance


# In[23]:


sns.countplot(df1['Is delivering now'])


# In[24]:


sns.countplot(df1['Switch to order menu'])

# Not singal one customers are moving switch to order menu


# In[25]:


sns.countplot(df1['Has Online delivery'])

# Around 2200 customers are ordering food online


# In[26]:


sns.countplot(x= "Rating color", hue="Price range", data=df1)


# # Understanding the Rating aggregate, color, and text.
# 
# Rating 0 — White — Not rated
# Rating 1.8 to 2.4 — Red — Poor
# Rating 2.5 to 3.4 — Orange — Average
# Rating 3.5 to 3.9 — Yellow — Good
# Rating 4.0 to 4.4 — Green — Very Good
# Rating 4.5 to 4.9 — Dark Green — Excellent

# In[27]:


sns.countplot(df1['Rating color'])

# Observations : 1 Maximum Rating 2.5 to 3.4 — Orange — Average for all the countries
# - Very few customers are rated Rating 0 — White — Not rated and Rating 1.8 to 2.4 — Red — Poor


# In[28]:


# Top 10 restarant with maximum number of outlets

x = df1['Restaurant Name'].value_counts().head(10).plot.bar(figsize =(12,6))

# observation :Maximum outlet is available for cafe coffee day in accoss the word


# In[29]:


# No of unique countries & number of restaurants listed in data set
df1.Country.value_counts()

## Observations : Maximum number of listings from india


# In[30]:


# Number of restaurant on zomato in diffrent cities in india

df1.loc[df1['Country'] == 'India'].City.value_counts().head(10)

# Maximum restaurant is in Delhi , Gurgaon , Noida and Faridabad. Other cities have almost equal distribution
# But significantly less as compared to Delhi , Gurgaon, Noida and Faridabad


# In[31]:


# Top 10 restaraunt with highest no of votes

max_votes = df1.Votes.sort_values(ascending = False).head(10)
df1.loc[df1['Votes'].isin(max_votes)][['Restaurant Name','Votes']]
df1.loc[df1['Votes'].isin(max_votes)][['Restaurant Name','Votes']].plot.bar(x = "Restaurant Name",y='Votes')

# Observation : We can see in the graph that the restaurants with maximum number of outlets are not the one which have highest number of votes. 
# The above list is totally different that our list of 10 restaurant with maximum number of outlets

    


# In[32]:


# HANDALE CATEGORICAL FEATURE with map method
df1['Has Table booking'] = df1['Has Table booking'].map({"Yes":1,"No":0})
df1['Is delivering now'] = df1['Is delivering now'].map({"Yes":1,"No":0})
df1['Switch to order menu'] = df1['Switch to order menu'].map({"Yes":1,"No":0})
df1['Has Online delivery'] = df1['Has Online delivery'].map({"Yes":1,"No":0})
df1['Rating color'] = df1['Rating color'].map({"Dark Green":1,"Green":2,"Yellow":3,"Orange":4,"White":5,"Red":6,"NaN":0})


# #  Droping colums which we will not use for the further analysis

# In[33]:


df1.drop(['Address'],axis=1,inplace = True)
df1.drop(['Locality'],axis=1,inplace = True)
df1.drop(['Locality Verbose'],axis=1,inplace = True)
df1.drop(['Latitude'],axis=1,inplace = True)
df1.drop(['Cuisines'],axis=1,inplace = True)
df1.drop(['Currency'],axis=1,inplace = True)
df1.drop(['Longitude'],axis=1,inplace = True)
df1.drop(['Rating text'],axis=1,inplace = True)
df1.drop(['City'],axis=1,inplace = True)
df1.drop(['Restaurant Name'],axis=1,inplace = True)


# In[34]:


df1.head(2)


# In[35]:


df1.dtypes


# In[36]:


df1.isnull().sum()


# In[37]:


df1.duplicated().sum()


# In[39]:


#Describe the data

df1.describe()

# Observations: Minimum cost of people in customrs for two people in different currencies


# # Correlation Plot - EDA

# In[40]:


#Correlation 

df1.corr()


# In[41]:


#Correlation plot

sns.heatmap(df1.corr())

