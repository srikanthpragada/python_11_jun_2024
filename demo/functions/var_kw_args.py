def show(*args, **details):
    for v in args:
        print(v)

    for k, v in details.items():
        print(k, v)


# def show2(**details, *args):
#       pass

show(10, 20, x=10)
show(a=10, b=20, msg="Hi")
show(x=1, y=20, r=30)

# show2(a = 10, b = 20, 30, 40)
