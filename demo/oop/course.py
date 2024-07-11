class Course:
    # static attributes or class attributes
    taxrate = 12

    # constructor - special method
    def __init__(self, title, fee, duration=30):
        # object attributes
        self.title = title
        self.fee = fee
        self.duration = duration

    # Methods
    def show(self):
        print(f'Title     : {self.title}')
        print(f'Fee       : {self.fee}')
        print(f'Duration  : {self.duration}')

    def getNetFee(self):
        return self.fee + self.fee * Course.taxrate // 100

    @staticmethod
    def getTaxrate():
        return Course.taxrate

class OnlineCourse(Course):
    def __init__(self, title, fee, onlineLink, duration = 30):
        super().__init__(title, fee, duration)
        self.onlineLink = onlineLink

    def show(self):
        super().show()
        print(self.onlineLink)



# Objects
c1 = Course("Python", 10000)
c2 = Course("Power BI", 15000)
c1.show()
print(c1.getNetFee())
print(Course.getTaxrate())
oc1 = OnlineCourse("Data Science", 20000, "http://www.abc.com/3934934", 36)
oc1.show()


c2 = Course("Power BI", 15000, 20)
