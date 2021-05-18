#!/usr/bin/env python
# coding: utf-8

# In[342]:


import numpy as np
import pandas as pd
import re


df = pd.read_csv('popular_movies.csv', na_filter= False, skipinitialspace=True)

# Convert values into int 
df['The Dig'] = pd.to_numeric(df['The Dig'])
df['Nomadland'] = pd.to_numeric(df['Nomadland'])
df['Minari'] = pd.to_numeric(df['Minari'])
df['The Father'] = pd.to_numeric(df['The Father'])
df['Nobody'] = pd.to_numeric(df['Nobody'])
df.to_csv('popular_movies.csv', index=False, mode='w')
    
df = pd.read_csv('popular_movies.csv')

# list out movie columns 
cols = ['The Dig' , 'Nomadland', 'Minari', 'The Father', 'Nobody']

# Calculate the user rating averages
user_0_avg = df.iloc[:1].sum(axis=1).div(len(cols)).to_string(header=None,index=False)
user_1_avg = df.iloc[1:2].sum(axis=1).div(len(cols)).to_string(header=None,index=False)
user_2_avg = df.iloc[2:3].sum(axis=1).div(len(cols)).to_string(header=None,index=False)
user_3_avg = df.iloc[3:4].sum(axis=1).div(len(cols)).to_string(header=None,index=False)
user_4_avg = df.iloc[4:5].sum(axis=1).div(len(cols)).to_string(header=None,index=False)

# Calculate the movie rating averages 
movie_0_avg = df.iloc[0:5, 1].sum(axis=0) / (len(cols))
movie_1_avg = df.iloc[0:5, 2].sum(axis=0) / (len(cols))
movie_2_avg = df.iloc[0:5, 3].sum(axis=0) / (len(cols))
movie_3_avg = df.iloc[0:5, 4].sum(axis=0) / (len(cols))
movie_4_avg = df.iloc[0:5, 5].sum(axis=0) / (len(cols))


#df.info()

#Append new columns with total averages for user and movie
df['Average Rating for User'] = [user_0_avg,user_1_avg,user_2_avg,user_3_avg,user_4_avg,'','','']
df['Average Rating for Movie'] = [movie_0_avg,movie_1_avg,movie_2_avg, movie_3_avg, movie_4_avg,'','','']


df.head()


# In[ ]:





# In[ ]:





# In[ ]:




