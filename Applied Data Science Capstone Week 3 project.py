#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

get_ipython().system('pip3 install bs4')

get_ipython().system('pip3 install lxml')

get_ipython().system('pip3 install html5lib')


# <font size=5>After importing libraries, we start to create Dataframe

# In[47]:


url = 'https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M'

df = pd.read_html(url,header=0)[0]
df


# <font size=5>We will need to drop all rows if values in column'Borough' are 'Not assigned'.
# <font size=5>Then check if there is any duplicated Postal Code

# In[46]:


df=df[df['Borough']!= 'Not assigned'].reset_index(drop=True)
df['Postal Code'].value_counts().sort_values() #check if there is any duplicated Postal Code


# <font size=5>Lookd like there is no duplicaed postal code.
# We also need to check if there is any value 'Not assigned' in column 'Neibourhood'

# In[45]:


df[df['Neighbourhood']=='Not assigned'] #check if there is any row 'Not assigned in Neibourhood column


# <font size=5>There is no value as 'Not assigned', so we print row#

# In[31]:


#there is no value as 'Not assigned', so we print row#
print('The number of rows is:',df.shape[0])


# 

# In[ ]:





# In[ ]:




