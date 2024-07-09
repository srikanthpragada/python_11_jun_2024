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


# Objects
c1 = Course("Python", 10000)
c2 = Course("Power BI", 15000)
c1.show()
print(c1.getNetFee())
print(Course.getTaxrate())
# print(c2.getTaxrate())


c2 = Course("Power BI", 15000, 20)
