def goldbach(n):
    def is_prime(n):
        if n < 4:
            return n > 1
        k = 2
        while k * k <= n:
            if n % k == 0:
                return False
            k += 1
        return True
    if n % 2:
        return []
    for x in range(2, n):
        if is_prime(x) and is_prime(n - x):
            return x, n - x
    return []

def sieve_of_eratosthenes(n):

    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    p = 2
    while p * p <= n:
        if primes[p]:

            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1

    return primes


def goldbach_conjecture(n):
    if n % 2 != 0 or n <= 2:
        return "Число должно быть четным и больше 2"

    primes = sieve_of_eratosthenes(n)

    for i in range(2, n // 2 + 1):
        if primes[i] and primes[n - i]:
            return [i, n-i]
    return []
