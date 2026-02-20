str = "abbcdcde"

dict = {}

for i in range(len(str)):
    if(str[i] in dict):
        dict[str[i]] += 1
    else:
        dict[str[i]] = 1

for i in str:
    if(dict[i] == 1):
        print("The First Non-Repeating Character is:",i)
        break