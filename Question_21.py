#!/usr/bin/env python
# coding: utf-8

# #Question 21
# 
# In a jupyter notebook solve the following question. Please upload the notebook to GitHub and provide the link submission box below.
# 
#  
# 
# __int()__: Constructor that takes as input a pair of Point objects that represent the ends points of the line segment
# 
# Length():: returns the length of the segment 
# 
# Slope() returns the slope of the segment of none if the slope is unbounded 
# 
#  
# 
# >>> p1 = Point(3,4)
# 
# >>> p2 = Point()
# 
# >>> s = Segment(p1,p2)
# 
# >>> s.length()
# 
# 5.0
# 
# >>> s.slope()
# 
# 0.75

# In[2]:


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


# In[29]:


class Segment:
    def __init__(self, Point1, Point2):
        self.Point1 = Point1
        self.Point2 = Point2
        
        
    def length(self):
            return ((self.Point2.x - self.Point1.x)**2 + (self.Point2.y - self.Point1.y)**2) ** 0.5
    
    def slope(self):
        if self.Point2.x - self.Point1.x == 0:
            return None
        
        return (self.Point2.y - self.Point1.y) / (self.Point2.x - self.Point1.x)** 0.75


# In[ ]:





# In[7]:





# In[32]:


# p1 = Point(3,4)
p1 = Point(3, 4)

#p2 = Point()
p2 = Point()

#s = Segment(p1,p2)
s = Segment(p1, p2)
s.length()


# In[33]:


print("Length is :", s.length())


# In[34]:


s.slope()


# In[35]:


print("Slope is:", s.slope()) 


# In[ ]:




