#!/usr/bin/env python
# coding: utf-8

# In[90]:


import pandas as pd


# In[91]:


df = pd.read_csv(r"C:\Users\Envy 360\Desktop\learn-data-analysis-w-python-master\learn-data-analysis-w-python-master\datasets\gradedata.csv")


# In[92]:


df.head()


# In[126]:


import matplotlib.pyplot as plt
df.plot()


# In[127]:


displayText = "Bob's 76 that says “Wow!"


# In[128]:


xloc = 1
yloc = df['grade'].max()
xtext = 8
ytext = -150


# In[129]:


plt.annotate(displayText,
             xy=(xloc, yloc),
             arrowprops=dict(facecolor='black',shrink=0.05),
             xytext=(xtext,ytext),
             xycoords=('axes fraction', 'data'),
             textcoords='offset points')


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




