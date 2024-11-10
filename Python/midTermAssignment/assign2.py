# Write a python program to create a function evaluateExpresion which should 
# return a=10 and b=45.Apply 3 different decorator , where first decorator must
# return expression “a+100*b*125” second decorator must return expression
# “a*a*b*b+100” and third decorator must return expression “b+a+b+175"

def decor1(fun):
    def inner():
        a,b=fun()
        return a+100*b*125
    return inner

def decor2(fun):
    def inner():
        a,b=fun()
        return a*a*b*b+100
    return inner

def decor3(fun):
    def inner():
        a,b=fun()
        return b+a+b+175
    return inner

def evaluateExpresion():
    a=10
    b=45
    return a,b

@decor1
def fun1():
    return evaluateExpresion()

@decor2
def fun2():
    return evaluateExpresion()

@decor3
def fun3():
    return evaluateExpresion()

print("The value of expression  a+100*b*125 is : ",fun1())
print("The value of expression  a*a*b*b+100 is : ",fun2())
print("The value of expression  b+a+b+175 is : ",fun3())