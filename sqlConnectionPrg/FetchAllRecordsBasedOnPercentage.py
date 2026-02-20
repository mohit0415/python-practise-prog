from Connection import mydb
from UserDTO import UserDTO
import json

myCursor = mydb.cursor(dictionary=True)

myCursor.execute("select * from student")

response = myCursor.fetchall()

users = []

for user in response:
    stud = UserDTO(user)
    x = stud.__percent__(user)
    if(x>=50):
        users.append(stud)

listOfDict = [user.__dict__() for user in users]

json_data = json.dumps(listOfDict)

print(json_data)




