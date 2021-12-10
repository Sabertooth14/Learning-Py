#!/usr/bin/env python
# coding: utf-8

# SETS

# In[4]:


first= set([33,55,65,22,33])


# In[5]:


first


# In[6]:


first.add(12)


# In[7]:


first


# In[8]:


sec=set('mississippi')


# In[9]:


sec


# Files

# In[1]:


get_ipython().run_cell_magic('writefile', 'newfile.txt', 'My name is Pranav.\nI am 19 years old.\nI live in Mumbai.')


# In[2]:


pwd


# In[7]:


open('newfile.txt')


# In[8]:


test=open('newfile.txt')


# In[9]:


test.read()


# In[10]:


test.readlines()


# In[11]:


test.seek(0)


# In[12]:


test.readlines()


# In[13]:


test.close()


# In[16]:


with open('newfile.txt')as myeg:
    cont=myeg.read()


# In[17]:


cont


# In[19]:


with open('newfile.txt','w')as myfile:
    myfile.write('I am tall')


# In[23]:


with open('newfile.txt','r')as f:
    print(f.read())


# In[26]:


with open('newfile.txt','a')as f:
    f.write("\nI like football ")


# In[27]:


with open('newfile.txt','r')as f:
    print(f.read())


# In[29]:


with open('newfile.txt','r+')as f:
    print(f.read())


# In[1]:


with open('newfile.txt','w')as f:
    f.write('\nMy name is Pranav')


# In[3]:


with open('newfile.txt','a')as f:
    f.write('\nI am 19 years old')


# In[4]:


with open('newfile.txt','r')as f:
    print(f.read())


# In[ ]:




