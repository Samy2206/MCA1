from threading import *
l=Lock()

class myThread():
    def fun1(self):
        l.acquire()
        for i in range(5):
            print("Child 1 ",i)
        
    def fun2(self):
        l.acquire()
        for i in range(5):
            print("child 2 ",i)
        l.release()
        l.release()

obj = myThread()
t1 = Thread(target=obj.fun1)
t2 = Thread(target=obj.fun2)
t1.start()
t2.start()
