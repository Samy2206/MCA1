#Create three arrays ane check the values from aray if similar print 'Equal Arrays' else print
#'Not Equal Arrays
import numpy as np
arr1=np.array([1,2,3,4])
arr2=np.array([1,2,3,4])
arr3=np.array([1,2,5,4])
res1=np.equal(arr1,arr2)
res2=np.equal(arr1,arr3)

#Method 1 using all()
# if all(res1==res2):
# if all(np.equal(arr1,arr2)==np.equal(arr1,arr3)):
#     print("Euals")
# else:
#     print("Not equal")

#method 2 using arry_equal()
if np.array_equal(res1,res2):
    print("Equal Arrays")
else:
    print("Not Equals")