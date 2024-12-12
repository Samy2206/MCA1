from threading import *
import time

class myThread(Thread):
    
    def run(self):
        for i in range(5):
            print("Child thread")
            
t1=myThread()
t1.start()
for i in range(5):
    print("main thread",i)
