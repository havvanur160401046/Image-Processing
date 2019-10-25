#!/usr/bin/env python
# coding: utf-8

# In[29]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
# if using a Jupyter notebook, inlcude:
get_ipython().run_line_magic('matplotlib', 'inline')
 


# In[30]:


data_path ="C:/minist.csv/"
train_data = np.loadtxt(data_path + "mnist_train.csv", 
                        delimiter=",")
test_data = np.loadtxt(data_path + "mnist_test.csv", 
                       delimiter=",") 


# In[31]:


image_size = 28 # width and length
no_of_different_labels = 10 #  i.e. 0, 1, 2, 3, ..., 9
image_pixels = image_size * image_size
data_path = "data/mnist/"
test_data[:10]


# In[32]:


test_data.ndim, test_data.shape


# In[33]:


test_data[10,0]


# In[34]:


im_3=test_data[10,:]


# In[41]:


im_3.shape


# In[46]:


im_4=im_3[1:]


# In[48]:


im_4.shape


# In[49]:


im_5=im_3.reshape(28,28)


# 

# In[50]:


m,n=test_data.shape
m,n


# In[55]:


10000 ,785 ; 1+ 28*28


# In[56]:


def my_counter(k=0):
    s=0
    for i in range(m):
        if(test_data[i,0]==k):
            s=s+1
    return s
for i in range(10):
    c=my_counter(i)
    print(i," ",c)


# In[57]:


eps=np.finfo(float).eps  #0 hatasını almamak için eps değerini ekliyoruz
import  math
def my_pdf_1(x, mu=0.0 , sigma=1.0):
    x= float(x -mu) / (sigma+eps) #1e-10
    return math.exp(-x*x/2.0) / math.sqrt(2.0*math.pi) / (sigma+eps)
my_pdf_1(10,1,3)


# In[58]:


def get_my_mean_and_std(k=0,l=350):
    s=0
    t=0
    
    for i in range(10000):  #ortalamayı buldurdu bizim satır m değerimiz 10000 oldugu için direk yazdık
        if(test_data[i,0]==k):
            s=s+1
            t=t+test_data[i,l+1]
           # digit_class=train_data[i,0]
            #top_left=train_data[i,1]
            #bottom_right=train_data[i,784]
           # print(digit_class,end=" ")
            #print(top_left,end=" ")
          #  print(bottom_right,end=" \n")      
    mean_1=t/s

    s=0
    t=0
    for i in range(10000):
        if(test_data[i,0]==k):
            s=s+1
            diff_1=test_data[i,l+1]-mean_1
            t=t+diff_1*diff_1
    #var_1=t/(s-1)
    std_1=np.sqrt(t/(s-1))

    #print(mean_1,std_1)
    return mean_1,std_1


# In[60]:


m_1,std_1=get_my_mean_and_std(k=,l=100)
m_1,std_1


# In[61]:


my_pdf_1(45.8,40,20)


# In[68]:


my_test_image=test_data[1,:]


# In[69]:


my_test_image.shape


# In[ ]:


my_test_image


# In[71]:


im_1=plt.imread("BirSayisi.png")
plt.imshow(im_1)
plt.show()


# In[72]:


im_1.shape


# In[73]:


im_2=im_1[:,:,0] #resmi 2 boyutlu hale getirdik
im_2.shape


# In[74]:


im_5=im_2.reshape(1,784) #im_2 yi 1 e 784 luk vektöre dönüştürdük


# In[75]:


im_5.shape


# In[77]:


get_my_mean_and_std(k=1,l=100)


# In[78]:


for i in range(10):
    pdf_t=0
    for j in range(784):
        x=im_5[0,j] #j nın gösterdiği pixel degeri var artık x de
        m_1,std_1=get_my_mean_and_std(i,j)
        
        pdf_deger=my_pdf_1(x,m_1,std_1+eps)
        pdf_t=pdf_t+pdf_deger
    print(pdf_t)
        


# In[96]:


n_array=[]
t=0
for i in range(10):
    pdf_t=0
    for j in range(784):
        x=im_5[0,j] #j nın gösterdiği pixel degeri var artık x de
        m_1,std_1=get_my_mean_and_std(i,j)
        
        pdf_deger=my_pdf_1(x,m_1,std_1+eps)
        pdf_t=pdf_t+pdf_deger
    print(pdf_t)
    n_array.insert(i,pdf_t)
ebe=n_array[0]    
for m in range(8):
    if n_array[m]>ebe:
        ebe=n_array[m]
        t=n_array.index(ebe)
print(t,ebe)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




