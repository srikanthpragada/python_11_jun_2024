import sys

length = 10

if len(sys.argv) < 2:
    print("Number is missing!. Please check usage given below!")
    print("Usage: python table.py <number> [length]")
    exit()

if len(sys.argv) > 2:
    length = int(sys.argv[2])


num = int(sys.argv[1])

for n in range(1, length + 1):
    print(f"{num:3} * {n:2} = {n*num:6}")

