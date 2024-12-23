# key = ['a','b','c','d']
# val = [1,2,3,4]
# res={}
# for i in range(len(key)):
#     res[key[i]]=val[i]
# print(res)

#write a program to square the number take input from user
# def square(num):
#     return num*num

# num=int(input("Enter  number"))
# result=square(num)
# print(result)

#write program to check if the number is even or not using function
# def number(num):
#     if num%2==0:
#         print("Number ",num,"is Even")
#     else:
#         print("Number ",num,"is odd")
# number(40)


# x=lambda num:num*num
# print(x(23))

# x=lambda num: "no is Even" if num%2==0 else "no is odd"
# print(x(13))

#homework
#use in reduce . map and filter using lambda function



#exception handling

# try:
#     num = 10/0
# except Exception as e:
#     print(e)
# finally:
#     print("Code is executed")


# try:
#     age = int(input("Enter your age"))
# except ValueError as e:
#     print(e)
# except Exception as e:
#     print(e)
# else:
#     if age>=18:
#         print("Eligible for voting")
#     else:
#         print("Not eligible for voting")
# finally:
#     print("Exection successful") 


