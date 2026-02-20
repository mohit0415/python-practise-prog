lst = ["Mohit","Sai","Kumar","Jyo"]


def countOfWords(lst):
    count = 0
    for i in lst:
        if(len(i)>4):
            count+=1
    return count

count = countOfWords(lst)

print("Count of Words: {} ".format(count))


