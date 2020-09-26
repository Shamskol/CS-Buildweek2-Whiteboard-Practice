def gensquares(n):
    for num in range(n):
        yield num**2

for x in gensquares(10):
    print(x)

def fib_with_generator(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        # a,b = b, a+b -> tuple unpacking instead of the three lines below!
        temp = a
        a = b
        b = temp+b

for num in fib_with_generator(10):
    print(num)    