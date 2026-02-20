dept = ['CSE','ECE','CSE','IT','IT','CSE','EEE','ECE','EEE','ECE']

dict = {}

for i in dept:
    if i in dict:
        dict[i] = dict[i] + 1
    else:
        dict[i] = 1

print(dict)