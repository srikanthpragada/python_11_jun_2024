# Print factors

num = int(input("Enter number :"))

for n in range(2, num // 2 + 1):
    if num % n == 0:
        print(n, end=' ')
