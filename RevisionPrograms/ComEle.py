a=[1,2,3]

b=[4,3,2,6,8]

c=[]

for i in range(len(a)):
    for j in range(len(b)):
        if(a[i] == b[j]):
            c.append(a[i])

print(c)