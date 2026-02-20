fn = lambda a: a*a*a

if __name__ == "__main__":
    print(fn(3))


# -----------------**-------------


lst = [1,67,45,32,41,24,76]

resLst = list(filter(lambda n : n%2==0,lst))

print(resLst)


responseLis = list(filter(lambda n : n%2==0,lst))

result = list(map(lambda n : n*2,responseLis))

print(result)