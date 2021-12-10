#!/usr/bin/env python
# coding: utf-8

# In[3]:


st="Pranv Karukayil"


# In[4]:


st.split()


# In[9]:


for x in st.split():
    print(x[2])


# In[12]:


list1=[(2,3),(5,6),(9,7)]
for a in list1:
    print(a)


# In[13]:


d={"k1":4,"k2":8,"k3":9}


# In[16]:


for x in d:
    print(x)


# In[17]:


d.items()


# In[18]:


d.values()


# In[20]:


for k,v in d. items():
    print(v)
    print(k)
    


# In[26]:


for k,v in d.items():
    print(k)


# In[28]:


list(d.keys())


# In[29]:


l2=[4,3,7,99,10]


# In[30]:


c=0;
for n in l2:
    c += n
    print (c)


# In[35]:


for w in "this is my house":
    print(w)


# In[34]:


for letter in 'This is a string.':
    print(letter)


# In[5]:


n=5
while(n>0):
    print(f"The number is {n}")
    n -= 1
else:
    print("Complete")


# In[1]:


n=0
while(n<5):
    print (n)
    n += 1
    if n==4:
        break


# In[2]:


s1="Pranav"
for letter in s1:
    if letter == "n":
        continue
    print(letter)


# In[3]:


s1="Pranav"
for letter in s1:
    if letter == "n":
        break
    print(letter)


# In[ ]:




