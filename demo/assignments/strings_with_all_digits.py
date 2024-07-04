
data = ["abc", "123", "xy1", "pqr4", "999"]

for v in filter(str.isdigit, data):
    print(v)
