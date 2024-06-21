names = ["Scotey", "Steve", "Hunter"]

chars = set()
for n in names:
    chars = chars | set(n)

print(chars)
