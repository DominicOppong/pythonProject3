

def fibo(n):
    x = 0
    y = 1
    print (x)
    print (y)
    for i in range (0,n):
        z = (x+y)
        x = y
        y = z
        print(z)

fibo(50)