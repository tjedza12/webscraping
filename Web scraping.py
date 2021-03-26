#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests


# In[2]:


from bs4 import BeautifulSoup as bs


# In[ ]:


github_user = input('Input Github User: ')


# In[4]:


url = 'https://github.com/'+github_user


# In[5]:


r = requests.get(url)


# In[6]:


soup = bs(r.content, 'html.parser')


# In[7]:


profile_image = soup.find('img', {'alt': 'Avatar'})['src']


# In[8]:


print(profile_image)


# In[ ]:




