# Write a python program to generate fibonnaci series using generator
def fibonacci(n):
    a=0
    b=1
    for i in range(n):
        yield a
        temp=b
        b=a+temp
        a=temp

fib_series=fibonacci(10)
for i in fib_series:
    print(i,end=' ')