#!/usr/bin/env python
# coding: utf-8

# In[23]:


print("GUESSING GAME")
print("Enter a number") 
print("You have to choose a number between 0 and 100")
print("If the number is close to the number th computer chose, it displays 'WARM' and if not it displays 'COLD'")
print("If u chose the same number the output will dispaly 'SUCCESS' and the number of guesses you take") 


# In[1]:


from random import randint


# In[2]:


n1= randint(0,100)


# In[3]:


count =1


# In[4]:


guess = []


# In[5]:


while True:
    n2 = int(input("Enter your guess: "))
    if (n2<0 or n2>100):
        print("OUT OF BOUNDS")
    else:
        guess.append(n2)    
        if(count == 1):
            if(abs(n1-n2)<30):
                print("WARM")
                count += 1
            else:
                print("COLD")
                count += 1
        elif(n2 != n1 and count>1):
            v = abs(n1 - guess[-1])
            d = abs(n1 - guess[-2])
            if(v<d):
                print("WARMER")
                count += 1
            else:
                print("COLDER")
                count += 1
        else:  
            print("SUCCESS")
            print(f"You took {count} guesses")
            break
    
            


# In[ ]:




