import time
from threading import *

def double(data):
    res=[]
    for i in data:
        time.sleep(1)
        res.append(i*2)
    return res

def square(data):
    res=[]
    for i in data:
        time.sleep(1)
        res.append(i*i)
    return res

n=[1,2,3,4,5,6]

st=time.time()
# t1=Thread(target=double,args=(n,))
# t2 = Thread(target=square,args=(n,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
double(n)
square(n)

et=time.time()
print("Time = ",et-st)