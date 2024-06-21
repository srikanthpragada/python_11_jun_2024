names = ["Scotey", "Steve", "Hunter"]

chars = set(names[0])
for n in names[1:]:
    chars = chars & set(n)

print(chars)
