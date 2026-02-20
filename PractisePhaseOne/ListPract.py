names=['Mohit','John','Smith','Alien']

print(names[0])
print(names[1])
print(names[0:3]);
print(names[-1:-3:-1])

nameNew = list(('Mohit','John','Smith','Alien'))

print(len(nameNew))

print(type(nameNew))

# ---change the element----

names[0]='Mohit Kumar'

print(names)

names[1:2] = ['John Doe','Alice']

print(names)

names.insert(2,"Bob")

print(names)

# ---add the elments---

names.append("Charlie")

print(names)

extraNames = ['Dave','Eve']

names.extend(extraNames)

print(names)


# --remove the items in the list---

names.remove("Bob")
print(names)

names.pop(3)

print(names)

names.pop()

print(names)

names.clear()
print(names)

# del names

# print(names)

x=5
y=6
print('x is', x,'y is',y)
c=x
x=y
y=c

numbers = [25,36,95,14,12,26]

# del numbers[2:5]

numbers[2:5] = []


print(numbers)

# --copy a List--

numbers2 = numbers.copy();
print(numbers2)

numbers2.append(100)

print(numbers2)
print(numbers)