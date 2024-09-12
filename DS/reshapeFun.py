#The element should be possible to be converted into 2D/3D
#reshape(array,(dimension))

import numpy as np

#reshape 1D to 2D
print("#reshape 1D to 2D")
data1 = np.array([10,20,30,40,50,60,70,80,90])
print(data1)
res1 = np.reshape(data1,(3,3))
print(res1)
print()

#reshape 1D to 3D
print("#reshape 1D to 3D")
data2=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(data2)
res2 = np.reshape(data2,(2,2,3))
print(res2)
print("")

#reshape 2D/3D to 1D
print("#reshape 2D/3D to 1D")
print(res1)
res3 = np.reshape(res1,-1)
print(res3)
print("")

#reshape 3D to 2D
print("#reshape 3D to 2D")
print(res2)
print("")
res4 = np.reshape(res2,(4,3))
print(res4)