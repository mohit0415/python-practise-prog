

def pattern():
    for i in range(5):
        print("*",end=" ")


def mainBlock():
    for i in range(5):
        pattern()
        print()

mainBlock()


def add(a,b):
    c=a+b
    print("The sum is:",c)

def inputs():
    x = int(input("Enter x:"))
    y= int(input("Enter y:"))
    add(x,y)

def mainBox():
    print("Welcome to addition Program")
    inputs()

mainBox()

def sum(a,*args):
    s=a
    for i in args:
        s+=i
    print("The sum is:",s)


sum(1,2,3,4,5)