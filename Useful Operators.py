#!/usr/bin/env python
# coding: utf-8

# In[8]:


for y in range(2,40,3):
     print(y)


# In[5]:


list(range(0,10,2))


# In[9]:


list(enumerate("aejwla"))


# In[11]:


w="Pranav"
for l in enumerate(w):
    print(l)


# In[12]:


for a,b in enumerate(w):
    print(a)
    print(b)


# In[13]:


l1=[1,2,3,4,5]
l2=["e","f","w","t","l"]
for m in zip(l1,l2):
    print(m)


# In[14]:


list(zip(l1,l2))


# In[15]:


for a,b in zip(l1,l2):
    print(b)


# In[16]:


4 in l2


# In[17]:


"b" not in l2


# In[18]:


min(l1)


# In[19]:


max(l2)


# IMPORTING

# In[21]:


t=[4,5,90,150]
from random import shuffle
shuffle(t)


# In[23]:


t


# In[24]:


from random import randint
randint(0,10)


# In[25]:


randint(0,100)


# Input

# In[26]:


input("Enter your name: ")


# In[27]:


input("number: ")


# In[28]:


r= int(input("number: "))


# In[29]:


r= float(input("n: "))


# In[30]:


type(r)


# In[2]:


from random import randint


# In[5]:


result=randint(2,30)


# In[6]:


result


# In[ ]:




