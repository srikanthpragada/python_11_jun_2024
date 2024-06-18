st = "How Do You Do"

for c in st:
    if ord(c) >= 65 and ord(c) <= 90:
        print(c)

for c in st:
    if c.isupper():
        print(c)