import time
from threading import *
def fun1(name):
    for i in range(5):
        time.sleep(1)
        print("Child thread ",name)


sT=time.time()
t1 = Thread(target=fun1,args=("sam",))
t1.start()
for i in range(5):
    time.sleep(1)
    print("main thread ",i)
t1.join()
eT=time.time()

print("Time: ",eT-sT)
