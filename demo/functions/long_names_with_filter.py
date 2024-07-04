def isLong(name):
    return len(name) > 5


names = ['Steven', 'Jack', 'Doresey', 'Mark', 'Richards']

for n in filter(isLong, names):
    print(n)

for n in filter(lambda v: len(v) > 5, names):
    print(n)
