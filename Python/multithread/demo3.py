from threading import *
import time
def square(data):
    res = []
    for i in data:
        time.sleep(1)
        res.append(i*i)
    print(res)
def cube(data):
    res = []
    for i in data:
        time.sleep(1)
        res.append(i*i*i)
    print(res)

startTime = time.time()

a=[1,2,3,4,5,6]

square(a)
cube(a)

endTime=time.time()

print("Time: ",endTime-startTime)


# from threading import *
# import time
# def square(data):
#     res = []
#     for i in data:
#         time.sleep(1)
#         res.append(i*i)
#     print(res)

# def cube(data):
#     res = []
#     for i in data:
#         time.sleep(1)
#         res.append(i*i*i)
#     print(res)

# startTime = time.time()

# a=[1,2,3,4,5,6]

# t1=Thread(target=square,args=(a,))
# t2=Thread(target=cube,args=(a,))

# t1.start()
# t2.start()

# endTime=time.time()

# print("Time: ",endTime-startTime)