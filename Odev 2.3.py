#!/usr/bin/env python
# coding: utf-8

# In[1]:


Ay_gunsayılı = [["Ocak","31"],["Şubat","28"],["Mart","31"],["Nisan","30"],["Mayıs","31"],["Haziran","31"],["Temmuz","31"],
                ["Ağustos","31"],["Eylül","30"],["Ekim","31"],["Kasım","30"],["Aralık","31"]]


# In[2]:


Aygun_icte2li = [[ Ay_gunsayılı[0][0],Ay_gunsayılı[1][0],Ay_gunsayılı[2][0],Ay_gunsayılı[3][0],Ay_gunsayılı[4][0],
        Ay_gunsayılı[5][0],Ay_gunsayılı[6][0],Ay_gunsayılı[7][0],Ay_gunsayılı[8][0],Ay_gunsayılı[9][0],Ay_gunsayılı[10][0],
        Ay_gunsayılı[11][0]],
                                                                                    
       [ Ay_gunsayılı[0][1],Ay_gunsayılı[1][1],Ay_gunsayılı[2][1],Ay_gunsayılı[3][1],Ay_gunsayılı[4][1],Ay_gunsayılı[5][1],
        Ay_gunsayılı[6][1],Ay_gunsayılı[7][1],Ay_gunsayılı[8][1],Ay_gunsayılı[9][1],Ay_gunsayılı[10][1],
        Ay_gunsayılı[11][1] ]]


# In[5]:


ilkbahar = [ Ay_gunsayılı[2], Ay_gunsayılı[3], Ay_gunsayılı[4]]
yaz = [Ay_gunsayılı[5], Ay_gunsayılı[6],Ay_gunsayılı[7]]
sonbahar = [Ay_gunsayılı[8],Ay_gunsayılı[9], Ay_gunsayılı[10]]
kış = [Ay_gunsayılı[11], Ay_gunsayılı[0], Ay_gunsayılı[1]]

mevsim_ayları = [ilkbahar, yaz, sonbahar, kış]


# In[8]:


yaz_guntoplam = int(yaz[0][1]) + int(yaz[1][1]) + int(yaz[1][1])
print(yaz_guntoplam)

