
#Multi threadign without using class

import threading,time

def fun1():
    for i in range(10):
        time.sleep(1)
        print("Hello ",i)

start=time.time()
# t1 = threading.Thread(target=fun1)
# t1.start()
for i in range(10):
    time.sleep(1)
    print("Main thread ",i)

fun1()
# t1.join()
end=time.time()

print("Time : ",end-start)
