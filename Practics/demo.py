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

# data = {'name':'Avani',
#         'age':'40',
#         'marks':'90'
#         }
    
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


# data = [1,2,3,4]   #create a list
# print(data)
# data.append(5)
# data.append(6)
# print(data)     #append

# list2 = [7,8,9,10]
# data.extend(list2)
# print(data)

# data[4]=100
# print(data)         #update

# data.insert(4,200)
# print(data)         #insert

# print(data.pop())
# print(data)

# data.remove(1)         #remove
# print(data)

# print(len(data))          #length

# print(data.count(4))

# write a program to take input from user to square a number and check different exceptions

# try:
#     num=int(input("Enter your input: "))
# except ValueError as e:
#     print(e)
# except TypeError as e:
#     print(e)
# except Exception as e:
#     print(e)
# else:
#     print(num*num)
# finally:
#     print("Execution completed")


#class

#varibale
# 1) local
# 2)global
# 3)static
# a=20    ----Global
# def fun(b=20):
#     a=10   ------Local

#     print(a)
# fun()
# print(a)


# def fun():
#     global a  #local varibel converted to global variable
#     a=10
#     print(a)

# fun()
# print(a)


#static
# class animal:
#     a=10
#     def __init__(self):
#         self.b=20

# obj=animal()
# print(obj.a)
# print(obj.b)

#Inheritance
#1) simple/single inheritance
#2) multiple inheritance
#3) multilevel 
#4) hierarchical
#5) hybrid

# class animal:
#     def bark(self):
#         print("DOg")

# class demo(animal):
#     pass

# obj = demo()
# obj.bark()


#multilevel

# class A:
#     def fun1(self):
#         print("A")

# class B(A):
#     # def fun1(self):
#     #     print("A")

#     def fun2(self):
#         print("B")

# class C(B):
#     # def fun1(self):
#     #     print("A")
    
#     # def fun2(self):
#     #     print("B")

#     def fun3(self):
#         print("C")              #A------------>B----------->C

# obj = C()
# obj.fun3()
# obj.fun1()
# obj.fun2()


#multiple

# class dog:
#     def dog(self):
#         print("Dog")

# class Cat:
#     def cat(self):
#         print("Cat")

# class Animal(dog,Cat):
#     def animal(self):
#         print("Animal")

# obj = Animal()
# obj.cat() 
# obj.dog()
# obj.animal()


#hybrid
        #             |A
        # ---------------------------
        # |           |              |
        # c1          c2              c3
        #             |
        #     -----------------
        #     |               |
        #     d1              d2

# class A:
#     def Dog(self):
#         print("hello")
# class C1(A):
#     def Cat(self):
#         print("hiii")
# class C2(A):
#     def Apple(self):
#         print("Apple")
# class C3(A):
#     def Banana(self):
#         print("Bnana")
# class d1(C2):
#     def Mango(self):
#         print("Mango")
# class d2(C2):
#     def Mangoes(self):
#         print("Mangoes")
# obj=A()
# obj1=C2()
# obj2=d1()
# obj2=d2()
# obj1.cat()
# obj1.Apple()
# obj1.Banana()
# obj1.Mango()
# obj1.Mangoes()


# class parent:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
    
#     def display(self):
#         print(self.name,self.age)

# class child(parent):
#     def __init__(self,marks,beauty,name,age):
#         super().__init__(name,age)
#         self.marks=marks
#         self.beauty=beauty

#     def display(self):
#         print(self.name,self.age,self.marks,self.beauty)

# obj=child(22,"Suvarna",90,"cute")
# obj.display()



#overloading and overidding

# def fun(a,b):
#     return a+b

# def fun(a,b,c):
#     return a+b+c

# def fun(a,b):
#     return a-b

# print(fun(10,20))



#operator oveloading
# str1="sam"
# str2=" bandrin"
# print(str1+str2)
# print(10+20)


# print(str1*3)
# print(10*20)


# class demo:
#     a=10
#     @staticmethod
#     def fun():
#         print("fun")

#     @classmethod
#     def fun2(cls):
#         print(cls.a)
        
# obj = demo()
# obj.fun()
# print(obj.a)

# python regex function

# 1. compile() : 
# 2. finditer()
# 3. match()
# 4. fullmatch()
# 5. search()
# 6. findall()
# 7. sub()

import re
# patter = re.compile("ab")           #create a pattern code
# match_found = patter.finditer('abbaababaabbaab')        #find iterations
# for i in match_found:             #return iterable obj
#     #start()
#     #end()
#     #group()
#     print(i.start(),"-----",i.end(),"---------",i.group())


# pattern  = re.compile('abcdabcd')
# match = pattern.match("abcdabcd")
# if match!=None:
#     print("data matched")
# else:
#     print(match)

# patter = re.compile("ab")           #create a pattern code
# match_found = patter.findall('abbaababaabbaab')        #find iterations
# print(match_found)

# patten
# 
#  = re.compile("ab")           #create a pattern code
# match_found = re.sub('a','b','abbaababaabbaab')        #find iterations
# print(match_found)



#create a pattern to identify pannumber
#EQSPA2858C
# 4 - alphabet
# 4 - num
# 1 - alpha


#DDFPA2858C

# import re
# pattern = r"^[A-Z]{5}\d{4}[A-Z]{1}"
# panNum = 'DDFPS2858C'

# mt = re.match(pattern,panNum)
# if mt != None:
#     print("Mathched")
# else:
#     print("Not matched")


#pattern for mobile number
#"+91 7776924312"


# import re
# pattern=r"^\+[0-9]{2}\s\d{10}$"
# mob="+91 7776924312"
# mt = re.match(pattern,mob)
# if mt != None:
#      print("Mathched")
# else:
#      print("Not matched")

#sanket_.-%+@gmail.com      {2,}