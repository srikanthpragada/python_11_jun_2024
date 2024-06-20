
st = "How are YOU"

codes = []
for c in st:
    if c.isupper():
        codes.append(ord(c))

print(codes)

codes = [ord(c) for c in st if c.isupper()]
print(codes)






