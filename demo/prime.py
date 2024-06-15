# Check whether number is prime

num = int(input("Enter number :"))

prime = True  # flag

for i in range(2, num//2 + 1):
    if num % i == 0:  # found factor
        print("Not prime")
        prime = False
        break


if prime:
    print("Prime")
