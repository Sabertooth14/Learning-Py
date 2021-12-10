#!/usr/bin/env python
# coding: utf-8

# In[1]:


def even_num(mlist):
    alleven=[]
    for no in mlist:
        if no%2==0:
            alleven.append(no)
        else:
            pass
        
        
    return alleven


# In[3]:


even_num([2,6,3])


# TUPLE UNPACKING

# In[4]:


player_price=[('CR7',125),('LM10',100),('PP6',80)]


# In[5]:


def tup_unpack(player_price):
    maxp=0
    player=""
    for a,b in player_price:
        if b>maxp:
            maxp=b
            player=a
        else:
            pass
        
    return(player,maxp)


# In[7]:


tup_unpack(player_price)


# INTERACTION BETWEEN FUNCTIONS: 3 CUP MONTE

# In[8]:





# In[9]:


from random import shuffle


# In[28]:


def shuffled_list(gamelist):
    shuffle(gamelist)
    return gamelist


# In[29]:


gamelist


# In[24]:


def playr_guess():
    guess=''
    
    guessing_list=['0','1','2']
    while guess not in guessing_list:
            guess=input("Pick a number form 0 to 2: ")
            
    return int(guess)


# In[25]:


playr_guess()


# In[51]:


def answr_check(gamelist,guess):
    if gamelist[guess]=='O':
        print("Congrats!! You guessed correctly")
    else:
        print("Wong answer...Better luck next time")
        print(gamelist)


# 

# In[57]:


answr_check(shuffled_list(gamelist),playr_guess())


# In[ ]:





# In[10]:


def myfunc(*args):
    mylist=[]
    for numbers in args:
        if numbers%2==0:
            mylist.append(numbers)
        else:
            pass
    return mylist


# In[11]:


myfunc(8,3,5,2)


# In[16]:


="Pranav"


# In[25]:



def myfunc(mystring):
    temp=""
    for i in range(0,len(mystring)):
        if i%2==0:
            temp = temp +mystring[i].upper()
        else:
            temp= temp + mystring[i].lower()
            
            
            
    return temp
        


# In[26]:


myfunc("Pranav")


# FUNCTIONS PRACTICE PROBLEMS

# In[22]:


def lesser_of_two(a,b):
    if a%2==0 and b%2 ==0:
        if(a>b):
            return b
        else:
            return a
    else:
        if(a>b):
            return a
        else:
            return b


# In[23]:


lesser_of_two(2,4)


# In[24]:


lesser_of_two(2,4)


# In[25]:


lesser_of_two(2,5)


# In[26]:


lesser_of_two(4,6)


# In[27]:


lesser_of_two(4,9)


# In[28]:


lesser_of_two(3,2)


# In[6]:


def animal_cracker(text):
  #  for t in range(0,len(text)):
      #  first=text[0]
    #    if text[t]==" ":
        #    second=text[t+1]
  #  if(first==second):
     #   return True
    #else:
   #     return False
      words=text.split()
      return words[0][0]==words[1][0]


# In[7]:


animal_cracker('Levelheaded Llama')


# In[8]:


animal_cracker('Crazy Kangaroo')


# In[33]:


def makes_twenty(a,b):
    if(a==20 or b==20) or (a+b==20):
        return True
    else:
        return False


# In[34]:


makes_twenty(20,10)


# In[35]:


makes_twenty(12,8)


# In[36]:


makes_twenty(5,6)


# In[9]:


def old_mcdonald(name):
  #  tp=""
   # for l in range (0,len(name)):
    #    if l==0 or l==3:
     #       tp=tp+name[l].upper()
       # else:
   #         tp=tp+name[l]
        
    #return tp
    firsthalf=name[:3]
    secondhalf=name[3:]
    return firsthalf.capitalize() + secondhalf.capitalize()


# In[10]:


old_mcdonald("macdonalds")


# In[11]:


def almost_there(n):
   # if(n in range(90,110) or n in range(190,210)):
    #    return True
    #else:
     #   return False
    return (abs(100-n)<=10) or (abs(200-n)<= 10)


# In[12]:


almost_there(104)


# In[13]:


almost_there(150)


# In[14]:


almost_there(209)


# In[23]:


def has_33(nums):
    for n in range(0,len(nums)-1):
        if(nums[n]==3 and nums[n+1]==3):
            return True
    return False
        
        


# In[24]:


has_33([1,3,3])


# In[25]:


has_33([1,3,1,3])


# In[26]:


has_33([3,1,3])


# In[40]:


def paper_doll(text):
    np=""
    for i in range (0,len(text)):
        np=np+text[i]*3
    return np


# In[41]:


paper_doll("Hello")


# In[42]:


paper_doll("Mississippi")


# In[18]:


def blackjack(a,b,c):
   # if(sum(a,b,c)<21):
   #     return sum(a,b,c)
    #elif(sum(a,b,c)>21):
     #   return "Bust"
    #elif(a==11 or b==11 or c==11):
     # return (sum(a,b,c)-10)
    if((a+b+c)<21):
        return (a+b+c)
    elif(((a+b+c)>21) and (a!=11 and b!=11 and c!=11)):
        return "Bust"
    elif((a==11 or b==11 or c==11) and ((a+b+c)>21)):
        return ((a+b+c)-10)


# In[19]:


blackjack(5,6,7)


# In[20]:


blackjack(9,9,9)


# In[21]:


blackjack(9,9,11)


# In[12]:


from math import sqrt

def count_prime(num):
    cp=0
    #i=1
    for n in range(1,num+1):
        count=0
        for j in range(1,num):
            if (n%j==0):
                count=count + 1
            else:
                pass
        if(count==2):
            cp=cp+1
    return cp
        


# In[13]:


count_prime(100)


# In[7]:


def spy_guess(nums):
    code=[0,0,7,'x']
    for n in nums:
        if n==code[0]:
            code.pop(0)
    return len(code)==1


# In[8]:


spy_guess([1,2,4,0,0,7,5])


# In[9]:


spy_guess([1,0,2,4,0,5,7])


# In[ ]:




