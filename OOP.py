#!/usr/bin/env python
# coding: utf-8

# In[20]:


class Dog():
    sound="Woof"
    
    def __init__(self,colour,name):
        
        
        self.colour=colour
        self.name=name
        
    def Age(self,n):
        
        print(f,"The age is {n}")


# In[13]:


mydog=Dog("Blue","Coco")


# In[14]:


type(mydog)


# In[15]:


mydog.colour


# In[16]:


mydog.name


# In[17]:


mydog.sound


# In[21]:


mydog.Age(2)


# In[25]:


class Square():
    
    def __init__(self,side=3):
        self.side=side
        
    def area(self):
        return self.side*self.side
    
    def peri(self):
        return 4*self.side


# In[26]:


shape=Square(6)


# In[27]:


shape.peri()


# In[28]:


shape.area()


# INHERITANCE
# 

# In[63]:


class Shape():
    
    def __init__(self,side):
        self.side=side
        
        print("A shape has been created")
        


# In[64]:


class Square(Shape):
    
    def area(self):
        return self.side*self.side


# In[73]:


class Circle(Shape):
    pi=3.14
        
    def area(self):
        return self.side*self.side*Circle.pi


# In[67]:


s=Shape(4)


# In[68]:


s.side


# In[74]:


p=Circle(2)
t=Square(5)


# In[75]:


p.area()


# In[72]:


t.area()


# SPECIAL METHODS

# In[108]:


class Player():
    
    def __init__(self,name,club,goals):
        
        self.name=name
        self.club=club
        self.goals=goals
        
    def __str__(self):
        
        return (f"The {self.name} is palaying for {self.club}")
     
    def __len__(self):
        
        return self.goals 
    
    def __del__(self):
        
        return "The palyer has retired"


# In[109]:


p=Player("Ronaldo","ManU",801)


# In[110]:


p.club


# In[111]:


str(p)


# In[112]:


len(p)


# In[114]:


del(p)


# HOME WORK

# In[8]:


class Cylinder():
    
    pi=3.14
    
    def __init__(self,height=1,radius=1):
        
        self.height=height
        self.radius=radius
        
    def volume(self):
        
        return self.height*self.radius*self.radius*Cylinder.pi
    
    def area(self):
        
        return (2*Cylinder.pi*(self.radius)**2)+(2*self.radius*self.height*Cylinder.pi)


# In[9]:


c=Cylinder(2,3)


# In[10]:


c.area()


# In[4]:


c.volume()


# In[18]:


class Line():
    
    def __init__(self,coor1,coor2):
        
        self.coor1=coor1
        self.coor2=coor2
        
    def distance(self):
        
        x1,y1=self.coor1
        x2,y2=self.coor2
        
        return ((x2-x1)**2 + (y2-y1)**2)**0.5
    
    def Slope(self):
        
        x1,y1=self.coor1
        x2,y2=self.coor2
        
        return ((x2-x1)/(y2-y1))


# In[19]:


l=Line((4,6),(3,5))


# In[20]:


l.distance()


# In[21]:


l.Slope()


# In[ ]:




