
total = count = 0

for i in range(10):
    num = int(input("Enter number [0 to stop]:"))
    if num == 0:
        break

    if num % 2 != 0:   # Odd number
        continue

    total += num
    count += 1

print("Total = ", total // count)