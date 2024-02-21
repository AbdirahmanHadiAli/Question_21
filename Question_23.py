#!/usr/bin/env python
# coding: utf-8

# In a jupyter notebook solve the following question using python. Please upload the notebook to GitHub and provide the link submission box below.
# 
# 
# 
# Develop a recursive function tough() that takes two nonnegative integer arguments and outputs a pattern as shown below.
# Hint: The first argument represents the indentation of the pattern, where the second argument -- always a pattern of 2 indicates the number stars(*)s in the longest line of *s in the pattern
# 

# >>> f(0,0)

# In[18]:


def tough(indentation, pattern_of_2):
    if pattern_of_2 == 0:
        return
    
    print(" " * indentation, end="")
    
    print("*" * (2 ** pattern_of_2))
    
    
    tough(indentation, pattern_of_2 - 1)



# In[20]:


tough(0, 4)


# In[19]:


tough(0, 5)


# In[ ]:




