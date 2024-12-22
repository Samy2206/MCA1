# data =[]
# for i in range(5):
#     temp = input("Enter your data: ")
#     data.append(temp)

# data = (num for num in input("Enter data").split(','))

# for i in data:
#     print(i)



# for i in range(5):
#     print("hii")
# print("Mine")


# i=0
# while i<=11:
#     print(i)
#     if i==10:
#         break
#     i+=1


# for i in range(1,11):
#     print(i)
#     if i ==10:
#         break

# str1 = "sammmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm"
# str2 = " mine"
# print(str1.count("m"))

#len count upper lower capatilize sum slice
# import numpy as np

# for i in range(1,11):
#     print(i,end=",")


#dictionary
# key : value

data = {'name':'Avani',
        'age':'40',
        'marks':'90'
        }
    
# for key,value in data.items():
#     print(key,"-->",value)

# val = data.values()
# print(val)

# key = data.keys()
# print(key)

# key = ['a','b','c','d']
# val = [1,2,3,4]

# res = {}

# # res["key"]="val"


# for i in range(len(key)):
#     res[key[i]]=val[i]

# print(res)


data = [1,2,3,4]   #create a list
print(data)
data.append(5)
data.append(6)
print(data)     #append

list2 = [7,8,9,10]
data.extend(list2)
print(data)

data[4]=100
print(data)         #update

data.insert(4,200)
print(data)         #insert

print(data.pop())
print(data)

data.remove(1)         #remove
print(data)

print(len(data))          #length

print(data.count(4))