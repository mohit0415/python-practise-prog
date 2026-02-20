i=1

while i<=5:
    j=1
    print("Telusko",end=" ")
    while j<=3:
        print("Python",end=" ")
        j=j+1
    print()
    i=i+1


# -----------------------

i=1
while i<=100:
    if (i % 3 == 0 or i % 5 == 0):
        i+=1
        continue
    print(i,end= " ")
    i=i+1


i=1
while i<=5:
    j=1
    while j<=4:
        print("#",end=" ")
        j=j+1
    print()
    i+=1
    
