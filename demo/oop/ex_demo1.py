
try:
    num = int(input("Enter number :"))
    print(100 / num)
except ValueError as ex:
    print("Sorry! Error : " + str(ex))
except ZeroDivisionError:
    print("Sorry! Zero is not valid!")
finally:
    print("Finally!")

print("The End")

