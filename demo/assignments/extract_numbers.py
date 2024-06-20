data = "abc 123 xyz 9383 de 292"

lst = []
for v in data.split(" "):
    if v.isdigit():
        lst.append(v)

print("-".join(lst))
