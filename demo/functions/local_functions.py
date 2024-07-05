g = 100  # Global variable


def fun1():
    a = 1  # Enclosing variable
    global g
    g = 1000

    # Local function
    def fun2():
        b = 2  # Local Variable
        nonlocal a
        a = 10
        print(g, a, b)

    fun2()
    print(a)


fun1()
