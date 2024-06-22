lst = ['red', 'blue', 'black', 'red', 'black', 'white']

colors = {}
for c in set(lst):
    colors[c] = lst.count(c)

print(colors)
