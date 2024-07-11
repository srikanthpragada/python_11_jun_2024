class Person:
    def __init__(self, name, email):
        self.name = name
        self.__email = email

    def getEmail(self):
        return self.__email

    @property
    def fullname(self):
        return self.name


p1 = Person("Kevin", "kevin@gmail.com")
print(p1.fullname)
# print(p1.__email)
print(p1._Person__email)
print(p1.__dict__)
