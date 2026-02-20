words = ["hi","hello","hey","python","code","IT"]

group_wrd = {}

for i in words:
    if len(i) in group_wrd:
        group_wrd[len(i)].append(i)
    else:
        group_wrd[len(i)] = [i]

print(group_wrd)
