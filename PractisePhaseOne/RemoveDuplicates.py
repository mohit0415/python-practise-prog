numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = []

for i in numbers:
    if i not in unique_numbers:
        unique_numbers.append(i)

print(unique_numbers)