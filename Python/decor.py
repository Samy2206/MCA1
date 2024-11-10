def decor1(fun):
    def inner(a,b):
        print(a*100+b*100)
    return inner

@decor1
def fun(a,b):
    print(a,b)


fun(10,20)
