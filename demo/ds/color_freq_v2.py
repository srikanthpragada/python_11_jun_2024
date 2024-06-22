lst = ['red','blue', 'black', 'red', 'black', 'white']

colors = {}

for c in lst:
    cnt = colors.get(c, 0)
    colors[c] = cnt + 1


print(colors)

