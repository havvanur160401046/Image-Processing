#!/usr/bin/env python
# coding: utf-8

# In[5]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt


# In[26]:


data_path ="C:/minist.csv/"
train_data = np.loadtxt(data_path + "mnist_train.csv", 
                        delimiter=",")
test_data = np.loadtxt(data_path + "mnist_test.csv", 
                       delimiter=",") 


# In[27]:


image_size = 28 # width and length
no_of_different_labels = 10 #  i.e. 0, 1, 2, 3, ..., 9
image_pixels = image_size * image_size
data_path = "data/mnist/"
test_data[:10]


# In[8]:


train_data.ndim, train_data.shape


# In[28]:


train_data[10,0]


# In[29]:


im_3=train_data[10,:]


# In[30]:


im_3.shape


# #### 

# In[31]:


im_4=im_3[1:]


# In[32]:


im_4.shape


# In[33]:


im_5=im_4.reshape(28,28)


# In[53]:


m,n=train_data.shape
m,n


# In[34]:


plt.imshow(im_5,cmap="gray")
plt.show()


# In[21]:


60000 ,785 ; 1+ 28*28


# In[35]:


m,n=train_data.shape
m,n


# In[37]:


def my_counter(k=0):
    s=0
    for i in range(m):
        if(train_data[i,0]==k):
            s=s+1
    return s
for i in range(10):
    c=my_counter(i)
    print(i," ",c)


# 

# In[50]:


import  math
def my_pdf_1(x, mu=0.0 , sigma=1.0):
    x= float(x -mu) / sigma
    return math.exp(-x*x/2.0) / math.sqrt(2.0*math.pi) / sigma
my_pdf_1(10,1,3)


# In[ ]:





# In[57]:


def get_my_mean_and_std(k=0,l=350):
    s=0
    t=0
    #l=350
    for i in range(m):  #ortalamayı buldurdu
        if(train_data[i,0]==k):
            s=s+1
            t=t+train_data[i,l+1]
           # digit_class=train_data[i,0]
            #top_left=train_data[i,1]
            #bottom_right=train_data[i,784]
           # print(digit_class,end=" ")
            #print(top_left,end=" ")
          #  print(bottom_right,end=" \n")      
    mean_1=t/s

    s=0
    t=0
    for i in range(m):
        if(train_data[i,0]==k):
            s=s+1
            diff_1=train_data[i,l+1]-mean_1
            t=t+diff_1*diff_1
    #var_1=t/(s-1)
    std_1=np.sqrt(t/(s-1))

    print(mean_1,std_1)
    return mean_1,std_1


# In[62]:


m_1,std_1=get_my_mean_and_std(2,100)
my_pdf_1(test_value,m_1,std_1)


# In[63]:


my_pdf_1()


# In[61]:


im_1=plt.imread("Birz.png")
plt.imshow(im_1)
plt.show()
test_value=im_1[0,0,0]


# In[ ]:




