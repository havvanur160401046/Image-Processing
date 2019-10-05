def my_f_1(my_list=[2,4,3,40,5,6,3,3,2,1]):
	toplam=0
	for i in my_list:
	    toplam+=i

	#hist=?
	mean=toplam/len(my_list)
	#print(mean)


	for i in my_list:
	    toplam=toplam+(i-mean)*(i-mean)

	var=toplam/(len(my_list)-1)
	#print(var)
	#std=?
	return mean,var

print(my_f_1())



my_histogram={}
my_list=[2,4,3,40,5,6,3,3,2,1]

for i in my_list:
	if i in my_histogram.keys():
		my_histogram[i]+=1
	else:
		my_histogram[i]=1

#my_histogram[1]=10
#my_histogram[2]=15
#my_histogram[40]=40
print(my_histogram)

import matplotlib.pyplot as plt
import numpy as np

def my_f_2(image_1=plt.imread('resim.jpg')):
	print(image_1.ndim,image_1.shape)
	m,n,p=image_1.shape
	my_histogram={}
	for i in range(m):
		for j in range(n):
			if (image_1[i,j,0] in my_histogram.keys()):
				my_histogram[image_1[i,j,0]]+=1
			else:
				my_histogram[image_1[i,j,0]]=0
			#image_1[i,j,1]
			#image_1[i,j,2]

	return my_histogram

print(my_f_2())


x=[]

y=[]
my_histogram=my_f_2()
for key in my_histogram.keys():
	x.append(key)
	y.append(my_histogram[key])

plt.bar(x,y)
plt.show()

