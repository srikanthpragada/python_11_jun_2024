
def zero(n):
    print(id(n))
    n = 0


a = 100
print(id(a))
zero(a)
print(a)

