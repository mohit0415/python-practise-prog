

def fib(n):
    a,b = 0,1
    print(a,end=" ")
    print(b,end=" ")
    for i in range(2,n):
        c= a+b
        print(c,end=" ")
        a=b
        b=c
    print()







def mainBlock():
    x=int(input("Enter length of the series:"))
    fib(x)


if __name__ == "__main__":
    mainBlock()