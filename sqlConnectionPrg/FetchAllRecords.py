from Connection import myCursor
import json

myCursor.execute("select * from student")

result = myCursor.fetchall()

class UserDTO:
    def __init__(self,id,name,age,m1,m2,m3):
        self.__id = id
        self.__name=name
        self.__age=age
        self.__m1=m1
        self.__m2=m2
        self.__m3=m3
    def __to_dict__(self):
        return {
            "id":self.__id,
            "name":self.__name,
            "age":self.__age,
            "m1":self.__m1,
            "m2":self.__m2,
            "m3":self.__m3
        }

users = []

for row in result:
    user=UserDTO(row[0],row[1],row[2],row[3],row[4],row[5])
    users.append(user)

usersDict = [user.__to_dict__() for user in users]

# print(usersDict)

json_data = json.dumps(usersDict)


print(json_data)