import numpy as np
 
#program to print even numbers upto n
            #Meth1
n = int(input("Enter Your Number: "))
data1=np.arange(0,n+1,2)        #for odd numbers -> arange(1,n+1,2)
print(data1)
            #Meth2
for i in range(0,n+1,2):        #for odd numbers -> range(1,n+1,2)
    print(i,end=" ")