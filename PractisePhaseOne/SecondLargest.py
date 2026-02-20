numbers = [10, 45, 23, 89, 12]

largest = numbers[0]

for num in numbers : 
    if num>largest:
        largest = num 

numbers.remove(largest)

second_largest = numbers[0]

for num in numbers :
    if num > second_largest:
        second_largest = num

print("The second Largest is :",second_largest)