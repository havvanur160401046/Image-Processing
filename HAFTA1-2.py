# -*- coding: utf-8 -*-
#Görüntü işleme dersleri 1
#import numpy as np
#list_2=np.ndarray([1,2,3,4,5])
#list_3=list_2+5
#print(list_3[0]) #her eleman 5 artmış şekilde olur. çalışmıyor.
########################################2
import os
import numpy as np
import mathplotlib.pyplot as plt
os.getcwd()
os.listdir() #kaynak adresi gösterir. işlenecek resim bu adresteki yere atılır.

jpg_files=[f for f in os.listdir() if f.endswith('.jpg')]
print(jpg_files)


im_1=plt.imread(jpg_files[0])
type(im_1)


im_1.ndim
im_1.shape
plt.imshow(im_1)
plt.show()

im_2=im_1[:,:,0]
plt.imshow(im_2)
plt.show()
plt.imsave('Merhabasonsinif.jpg',im_2)

im_3=plt.imread('test.jpg')

print(type(im_3))
print(im_3.ndim) #boyut
print(im_3.shape) #boyutlardaki size
print(im_3[100,100,:])

m,n,p=im_3.shape

#resmi gri yapma
new_image=np.zeros((m,n),dtype=float)
for i in range(m):
    for j in range(n):
        s=(im_3[i,j,0]+im_3[i,j,1]+im_3[i,j,2])/3
        new_image[i,j]=s
plt.imshow(new_image,cmap="gray")
plt.imshow(new_image,cmap="gray")
plt.show()
plt.imsave('test_2.png',new_image,cmap='gray')

#90 derece döndürme
new_image=np.zeros((m,m),dtype=float)
for i in range(m):
    for j in range(n):
        s=(im_3[i,j,0]+im_3[i,j,1]+im_3[i,j,2])/3
        new_image[j,i]=s
plt.imshow(new_image,cmap="gray")
plt.show()
plt.imsave('test_3.png',new_image,cmap='gray')

######################
#im_2=im_1+25 parlaklık arttırır.
#im_3=255-im_1 renkleri ters çevirir.
########
#renk ters çevirme fonksiyonu
def my_inverse(im_1):
    return(255-im_1)
    














