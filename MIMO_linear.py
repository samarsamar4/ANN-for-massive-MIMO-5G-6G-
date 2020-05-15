#!/usr/bin/env python
# coding: utf-8

# <h1 style="color:#191970; font-size:38px">MIMO-Linear</h1>

# <h1 style="color:#006400">Libraries</h1>

# In[1]:


import numpy as np
from commpy.modulation import QAMModem
from numpy.linalg import inv


# <h1 style="color:#006400">Variables</h1>

# In[2]:


Mr = 10
Mt = 100
M = 16
N_bits = Mr * np.log2(M)


# <h1 style="color:#006400">Initialization</h1>

# In[3]:


NMSE=[]


# ### Generate Random bits 

# In[4]:


for i in range(2, 100):
    bits = np.random.randint(2, size=int(N_bits))


# ### 16-QAM Modulation

# In[5]:


QAM16 = QAMModem(16)
Z=QAM16.modulate(bits)
print(Z)


# ### Generate Channel Matrix

# In[6]:


H = (1 / np.sqrt(2 * Mt)) * (np.random.randn(Mr, Mt) + 1j * np.random.randn(Mr, Mt))


# ### Demodulation 

# In[7]:


zf=np.transpose(np.conj(H)).dot(inv(H.dot(np.transpose(np.conj(H)))))
x_zf=zf.dot(Z)
recieve=H.dot(x_zf)
A=QAM16.demodulate(recieve, demod_type='hard', noise_var=0) 
print(bits)
print(A)
print(Z.T)


# <h1 style="color:#006400">Mean Squared Error </h1>

# In[8]:


NMSE.append(np.mean(np.abs(Z - recieve) ** 2) / np.mean(np.abs(Z) ** 2))
NMSEdb = 10 * np.log10(np.mean(NMSE))
print(NMSEdb)

