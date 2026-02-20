
def sum(s,*args):
    print(s)
    print(args)


sum(1,2,3,4,5)

# ---The args is of tuple type---

def personData(name,**data):
    print(name)
    print(data)


personData("John",age=30,city="Hyderabad")