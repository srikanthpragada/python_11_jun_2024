lst = ['red','blue', 'black', 'red', 'black', 'white']

colors = {}

for c in lst:
    if c in colors:
        colors[c] = colors[c] + 1
    else:
        colors[c] = 1


print(colors)

