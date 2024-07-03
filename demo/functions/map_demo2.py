def extract_upper(s):
    st = ""
    for c in s:
        if c.isupper():
            st += c

    return st


def extract_upper2(s):
    return "".join(filter(str.isupper, s))


data = ["Abc", "XYZ", "PqR", "DEf"]

# for n in map(str.isupper, data):
#     print(n)

for n in map(extract_upper2, data):
    print(n)
