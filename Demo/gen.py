def nogen(data):
    res=[]
    for i in data:
        res.append(i*2)
    return res

def gen(data):     #3
    for i in data:
        yield i*2           #iterable object




data=[3,5,67,8,965,5] #1

res = gen(data) #2

print(next(res))
print(next(res))


print("-----------------")

for i in res:
    print(i)

print("---------------")

for i in res:
    print(i)