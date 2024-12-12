
# num=int(input("Enter input: 20"))

# result=lambda x:x*x
# print(result(num))



def sqr(num):
    return(num*2)


# a=[1,2,3,4]
# res=list(map(sqr,a))
# print(res)

# num=[2,3,4,5,6]
# def myFuc(x):
#     if x<3:
#         return False
#     else:
#         return True


# numbers=filter(lambda x:x>3,num)


# for x in numbers:
#     print(x)

# import functools
# list=[1,2,3,4]
# print(functools.reduce(lambda x,y:x+y,list))
def genFun():
    for i in range(5):
        yield input("enter name")
        
x=genFun()
for i in x:
    print(i)
