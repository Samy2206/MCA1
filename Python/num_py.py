#Only number data is allowed in numpy
#This is used for performing mathematical functions
#Multi-dmentional array is allowed

import numpy as np      #numpy is a library

data1 = np.array([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])   
print(data1)

data2=np.zeros(5)   #To create all zeros
print(data2)

data3=np.ones(5)    #To create array with all ones
print(data3)

data4=np.arange(0,11,2)  #arange to create array within specified range
print(data4)             #arange(start,end-1,jump)

data5=np.array([[10,20,30],[40,50,60],[70,80,90]])      #create 2D array
print(data5)
data6=np.zeros([3,3])       #create 2D array with all zeros
print(data6)

data7=np.array([[[10,20,30],[40,50,60],[70,80,90]],[[1,2,3],[4,5,6],[7,8,9]],np.zeros([3,3])])      #Create 3D array
print(data7)

data8=np.zeros([2,3,3])     #Create 3D array in all zeros
print(data8)