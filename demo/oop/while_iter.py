
l = [1,2,3]

# for n in l:
#     print(n)

li = iter(l)  # l.__iter__()
while True:
    try:
        n = next(li)   # li.__next__()
        print(n)
    except:
        break




