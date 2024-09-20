import array as arr
data=arr.array('i',[10,20,30,40])
#print(data)
#for var in data:
#    print(var)

# data[1]=22
# data.append(25)
# data.extend([50,60,70])
# print(data)
# data.pop(3)
# print(data)
data1=arr.array('i',[50,60,70,80])
newdata=arr.array('i')
newdata=data+data1
print(newdata)

print(newdata[:5])

# for var in newdata:
#     print(var)