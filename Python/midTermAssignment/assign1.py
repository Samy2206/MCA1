# Explain generator with the help of example where generate series
# of numbers from 1 to 7

def generator():
    for i in range(1,8):
        yield i
    
res=generator()
for i in res:
    print(i)