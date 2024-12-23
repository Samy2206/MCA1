#lock
#1.Lock
#2.RLock
#3.Semahore

from threading import *

# l=Lock()
# def fun(name):
#     l.acquire()
#     for i in range(10):
#         print(name)
#     l.release()

# t1= Thread(target=fun,args=("sam",))
# t2= Thread(target=fun,args=("Sandesh",))
# t1.start()
# t2.start()

# # for i in range(10):
# #     print("main Thread")


# l=RLock()

# def fact(num):
#     l.acquire()
#     if num<=0:
#         l.release()
#         return 1
#     else:
#         l.release()
#         return num*fact(num-1)
        
    
    

# def fun(num):
#     print(fact(num))

# t1 = Thread(target=fun,args=(5,))
# t2 = Thread(target=fun,args=(10,))
# t1.start()
# t2.start()



#semaphore 

l=Semaphore(2)
def fun(name):
    l.acquire()
    for i in range(10):
        print(name)
    l.release()

t1= Thread(target=fun,args=("sam",))
t2= Thread(target=fun,args=("sanjana",))
t3= Thread(target=fun,args=("siddhant",))
t4= Thread(target=fun,args=("Sandesh",))
t1.start()
t2.start()
t3.start()
t4.start()
