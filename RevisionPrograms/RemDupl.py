nums = [1,2,2,3,4,4,5]

distinct = []

for i in nums:
    if i not in distinct:
        distinct.append(i)

print(distinct)

unique=[]

for i in range(len(nums)):
    if nums[i] not in unique:
        unique.append(nums[i])

print(unique)