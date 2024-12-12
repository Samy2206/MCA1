from threading import *
class myThread(Thread):
    def run(self):
        for i in range(5):
            print("Child thread ",i)

t1 = myThread()
t1.start()

for i in range(5):
    print("Main Thread ",i)
