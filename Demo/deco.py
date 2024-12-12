# def mydecor(fun):           #3
#     def inner():
#         print("Before")         #4
#         fun()
#         print("After")          #6
    
#     return inner


# @mydecor            #2
# def fun():
#     print("Function")           #5
#     # print("Before")         #4
#     #     fun()
#     #     print("After") 


def decor2(Shubh):
    def inner(name):
        if name=="sandesh":
            print("Sanjana")
        else:
            Shubh(name)
    return inner
        
@decor2
def fun1(name):
    print("Hello")



fun1('sandesh')   #1