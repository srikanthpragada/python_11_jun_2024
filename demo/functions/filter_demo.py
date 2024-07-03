def ispositive(n):
    return n > 0


nums = [10, -30, 50, -33, -44]

for n in filter(ispositive, nums):
    print(n)



