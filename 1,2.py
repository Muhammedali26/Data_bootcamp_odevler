#!/usr/bin/env python
# coding: utf-8

# In[1]:


x = 1000
a = 1000
y = 12
for n in range(7):
 a = a + (a * y / 100)
print(a)


# In[2]:


metin = "Hafta başında {} dolarlık bitcoin aldığımızda günde ortalama %{} kazançla, bir hafta sonunda {:.2f} dolar kazanırdık"
print (metin.format(x,y,a))


# In[ ]:




