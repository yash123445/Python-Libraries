#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt


# In[3]:


import numpy as np


# In[4]:


x=np.array([1000,2000,3000,4000,5000])
y=np.array([10,20,30,40,50])

plt.title("Relationship Between Area and Price", color='r')
plt.xlabel("SALES(sq.ft)",color='r',)
plt.ylabel("Price(lakhs)",color='r')

plt.plot(x,y,marker='*',color='r')
plt.grid(axis='x',color='w',linestyle='-',linewidth=1)
plt.show()


# In[5]:


xpoints=np.array([5,15])
ypoints=np.array([0,150])
plt.plot(xpoints,ypoints)
plt.show()


# In[6]:


xpoints=np.array([10,20])
ypoints=np.array([5,10])

plt.plot(xpoints,ypoints,'+')    ## we can denote the points by the marker
plt.show()


# In[7]:


ypoints=np.array([12,10,16,18])

plt.plot(ypoints, marker='o')
plt.show()


# In[9]:


ypoints=np.array([1,3,5,3])
plt.plot(ypoints , '*:k')               ## coloun signifies the dotted line and k signifies the black colour
plt.show()


# In[8]:


plt.plot(ypoints,'*')
plt.show()                  ## if we do not specify the marker then it only shows  the points


# In[10]:


xpoints=np.array([12,13,14,15])
ypoints=np.array([10,12,14,16])
plt.plot(xpoints,ypoints,marker='x',color='r',ms=10)       ## ms defines the marker size
plt.show()


# In[11]:


ypoints=np.array([12,10,16,18])

plt.plot(ypoints, marker='o',ms=20,mec='r')                       ## mec defines the age colour of marker 
plt.show()

