users = [
    {"name": "A", "age": 25},
    {"name": "B", "age": 17},
    {"name": "C", "age": 30}
]

adults  = list(filter(lambda user : user["age"] >= 18,users))

adultsNames = list(map(lambda user : user["name"],adults))

print(adultsNames)



students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78}
]

passedStudents = list(filter(lambda student : student["grade"] >=80,students))

passedStudentsNames = list(map(lambda students : students["name"],passedStudents))

print(passedStudentsNames)


num = [-1, 2, -3, 4, 5]

postiveNums = list(filter(lambda n : n>0,num))

reCheckedResult = list(map(lambda n : n*2,postiveNums))

print(reCheckedResult)
