
def numbers():
    for n in range(5):
        print("Came here!")
        yield n


n = numbers()
print(type(n))
print("Starting")
print(next(n))
print(next(n))
for v in n:
    print(v)



