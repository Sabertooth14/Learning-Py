#!/usr/bin/env python
# coding: utf-8

# Dictionaries

# In[1]:


p={'name':'Pranav','age':19,'ht':178,'wt':65}


# In[2]:


p


# In[3]:


p['ht']


# In[5]:


p['name']


#  d={'k1':[3,6,9],'k2':['a','B','c']}

# In[9]:


d['k1'][1]


# In[12]:


d['k2'][1].lower()


# In[13]:


d


# In[19]:


d['k2'].pop()


# In[3]:


d={'k1':['a','b','c']}


# In[5]:


d['k1'][0].upper()


# In[6]:


d


# In[8]:


d['k1'].pop()


# In[9]:


d


# TUPLES

# In[2]:


t=(3,5,3,2,66,7,3)


# In[3]:


t.count(3)


# In[4]:


t.index(3)


# In[5]:


t[4]


# In[6]:


t[3:6:2]


# In[7]:


t[3]


# In[10]:


mylist=[]
for items in t:
    if items%2==0:
        mylist.append(items)
    else:
        pass


# In[11]:


mylist


# In[ ]:




