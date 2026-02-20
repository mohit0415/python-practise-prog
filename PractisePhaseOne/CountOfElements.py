numbers = [1, 2, 2, 3, 3, 3]

count = {}

for i in numbers:
    if i in count:
        count[i] = count[i] + 1
    else:
        count[i] = 1

print(count)