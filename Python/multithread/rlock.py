from threading import *
l=RLock
def fact(n):
    l.acquire()
    if n==0:
        l.release()
        return 1
    else:
        l.release()
        return n*fact(n-1)


t1 = Thread(target=fact,args=(5,))
t2 = Thread(target=fact,args=(9,))

t1.start()
t2.start()