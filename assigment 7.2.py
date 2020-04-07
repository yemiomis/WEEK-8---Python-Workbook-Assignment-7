#!/usr/bin/env python
# coding: utf-8

# In[136]:


import matplotlib.pyplot as plt


# In[137]:


import pandas as pd


# In[138]:


names = ['Bob','Jessica','Mary','John','Mel']


# In[139]:


status = ['Senior','Freshman','Sophomore','Senior','Junior']


# In[140]:


grades = [76,95,77,78,99]
GradeList = zip(names,grades)


# In[141]:


df = pd.DataFrame(data = GradeList,columns=['Names', 'Grades'])


# In[145]:


get_ipython().run_line_magic('matplotlib', 'inline')
df.plot(kind='bar')
df.plot(title='status')


# In[ ]:





# In[ ]:





# In[ ]:





# 

# In[ ]:


# no the R2 remains the same 


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




