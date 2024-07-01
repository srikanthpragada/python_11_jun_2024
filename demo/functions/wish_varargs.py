def wish(*names, message="Hello"):
    print(type(names))
    for n in names:
        print(message, n)


def greet(message, *names):
    for n in names:
        print(message, n)


wish("Andy", "Jack", "Mark", message="Hi")
wish("Scott", "Steve")
greet("Hi", "b", "c")


