from Connection import mydb
import json

myCursor = mydb.cursor(dictionary=True)

myCursor.execute("select * from student")

response = myCursor.fetchall()

print(response)

class myDTO:
    def __init__(self,row):
        self.__m1=row['marks1']
        self.__m2=row['marks2']
        self.__m3=row['marks3']
        self.__name=row['name']
        self.__age=row['age']
    def __toDict__(self):
        return {
            'name':self.__name,
            'age':self.__age,
            'm1':self.__m1,
            'm2':self.__m2,
            'm3':self.__m3
        }
    def checkAge(self,row):
        if(row['age'] >=18):
            return True
        else:
            return False


users=[]

for row in response:
    if(row['age'] >= 18):
        user = myDTO(row)
        users.append(user)

jsonData = [user.__toDict__() for user in users]

JSON_DATA = json.dumps(jsonData)
print(JSON_DATA)
