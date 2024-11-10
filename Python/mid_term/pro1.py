# Write a python program to create a function originalfunc which should return a 
# message “I am a function kindly decorate my content”. Implement decorator on the 
# function.

def decor(fun):
    def inner():
        print("Before originalFunc")
        fun()
        print("After originalFunc")
    return inner

@decor
def originalFunc():
    print("I am a function kindly decorate my content")

originalFunc()