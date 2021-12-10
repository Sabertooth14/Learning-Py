#!/usr/bin/env python
# coding: utf-8

# In[3]:


mylist=[5.33,6,99,'pranav']


# In[4]:


mylist[3]


# In[5]:


mylist[2]=69


# In[7]:


mylist


# In[9]:


mylist.append('pk')


# In[10]:


mylist


# In[11]:


mylist.pop(1)


# In[12]:


mylist


# In[13]:


nlist=[0.5,7.2,5.3,2.2]


# In[14]:


nlist.sort()


# In[15]:


nlist


# In[16]:


nlist.reverse()


# In[17]:


nlist


# In[18]:


nlist[2:]


# In[19]:


nlist[:3]


# In[20]:


nlist[1::2]


# In[21]:


len(mylist)


# In[22]:


len(nlist)


# LIST COMPREHENSION

# In[1]:


y2=[letter for letter in "Pranav" ]


# In[2]:


y2


# In[3]:


x1=[n for n in range(0,10) ]


# In[4]:


x1


# In[5]:


a=[n**2 for n in range(0,5)]


# In[6]:


a


# In[7]:


l=[x-y for x in [12,13,14] for y in [8,9,10]]


# In[8]:


l


# In[ ]:




