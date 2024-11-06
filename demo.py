def decor(fun):
    def inner(name):
        print("Hello")
        fun()
        print("Hii")
    return inner

@decor
def fun(name="Sam"):
    print(name)

fun("SAM")