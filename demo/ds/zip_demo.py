l1 = [1, 2, 3]
l2 = [10, 20, 30, 40]

for t in zip(l1, l2, "abcd", (100, 200)):
    print(t)

# for t in zip(l1, l2, strict=True):
#     print(t)
