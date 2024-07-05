import sys

if len(sys.argv) < 2:
    print("Missing number. Please provide number on command line")
    exit()

num = int(sys.argv[1])

for n in range(1, 11):
    print(f"{num:3} * {n:2} = {n*num:6}")

