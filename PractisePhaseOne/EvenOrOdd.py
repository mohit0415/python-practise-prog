numbers = [1, 2, 3, 4, 5, 6]

even = 0
odd = 0
for i in numbers:
    if(i % 2 == 0):
        even += 1
    else:
        odd += 1

print("Even num :",even)
print("Odd",odd)