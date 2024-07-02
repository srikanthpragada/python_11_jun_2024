def operation(func, value):
    func(value)


def show(message):
    print("Message->", message)

operation(print, 100)
operation(show, "Hi")

