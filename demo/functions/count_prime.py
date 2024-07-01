def isprime(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False

    return True


def count_prime(lst):
    count = 0
    for n in lst:
        if isprime(n):
            count += 1

    return count


cnt = count_prime([12, 37, 89, 75])
print(cnt)
