from threading import *
import time

class myThread:
    def fun1(self):
        time.sleep(0.001)
        for i in range(10):
            print("Chlild thread",i)

start = time.time()
obj=myThread()
t1=Thread(target=obj.fun1)
t1.start()

for i in range(10):
    time.sleep(0.001)
    print("Main Thread",i)

t1.join()
end = time.time()

print("Time: ",end-start)