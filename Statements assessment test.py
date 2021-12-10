#!/usr/bin/env python
# coding: utf-8

# In[12]:


st= "Print only the words that start with s in this sentence"


# In[14]:


st.split()


# In[11]:


for word in st.split():
    if word[0] == 's':
        print(word)


# In[4]:


st


# In[16]:


for n in range(0,11,2):
    print(n)


# In[17]:


mlist=[n for n in range(0,51) if n%3==0]


# In[18]:


mlist


# In[5]:


st = 'Print every word in this sentence that has an even number of letters'


# In[22]:


for w in st.split():
    if len(w)%2==0:
        print(w+ "is even")


# In[25]:


for n in range(0,100):
    if(n%3==0 and n%5==0):
        print("FizzBuzz")
    elif n%3 ==0:
        print("Fizz")
    elif n%5==0:
        print("Buzz")
    else:
        print(n)


# In[26]:


st = 'Create a list of the first letters of every word in this string'


# In[27]:


[w[0] for w in st.split()]


# In[ ]:




