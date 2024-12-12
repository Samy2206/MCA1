#multithreading with extending thread class
from threading import *
import time

class myThread(Thread):
    def f1(self):
        print("Hello")
    
    def run(self):
        for i in range(10):
            time.sleep(1)
            print("Child thread ",i)

start = time.time()
t1 = myThread()
t1.start()
for i in range(10):
    time.sleep(1)
    print("Main thread ",i)

t1.join()
end = time.time()

print("Time : ",end-start)
