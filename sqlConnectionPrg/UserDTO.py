class UserDTO:
    def __init__(self,row):
        self.__name = row['name']
        self.__age = row['age']
    def __dict__(self):
        return {
            'name': self.__name,
            'age': self.__age
        }
    def __percent__(self,row):
        x = ((row['marks1'] + row['marks2'] + row['marks3'] )/ 300) * 100
        return x
