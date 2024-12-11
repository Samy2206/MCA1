# def sqr(num):
#     return num*num


# print(sqr(10))

# res = lambda num: num*num
# print(res(10))


# filter map reduce

# def even(num):
#     if num%2==0:
#         return num



# res = filter(even,a)
# for i in (res):
#     print(i)



# map(fun,iterable)
a=[2,4,6,4,7,78]



# def sqr(data):
#     res=[]
#     for i in data:
#         res.append(i*i)
#     return res

# print(sqr(a))

res=[]
res = (map(lambda x:x*x,a))
for i in res:
    print(i)   
