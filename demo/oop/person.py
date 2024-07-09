class Person:
    def __init__(self, name, email):
        self.name = name
        self.__email = email

    def getEmail(self):
        return self.__email

p1 = Person("Kevin", "kevin@gmail.com")
#p1.__email = "kevin@yahoo.com"
print(p1._Person__email)
print(p1.__dict__)

