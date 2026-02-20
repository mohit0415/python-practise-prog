from array import *

arr = array('i', [])

lens = int(input("Enter the size of an array:"))

for i in range(lens):
    x = int(input("Enter the Number:"))
    arr.append(x)

print(arr)

key = int(input("Enter the  key:"))

for i in range(len(arr)):
    if(arr[i] == key):
        print("Key found at",i)
        break
else:
    print("Key not found")