from threading import *
import time
l=Lock()

def wish(name):
    l.acquire()
    for i in range(5):
        print("Hello",end=" ")
        time.sleep(0.1)
        print(name)
    l.release()
st=time.time()
t1 = Thread(target=wish,args=('Dhoni',))
t2 = Thread(target=wish,args=('Virat',))
t1.start()
t2.start()
t1.join()
t2.join()
et=time.time()
print("Time:",et-st)
