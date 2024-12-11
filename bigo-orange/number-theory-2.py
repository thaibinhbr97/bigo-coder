"""
Number Theory 2

Sieve of Eratosthenes & Euler's Totient Function
"""


def isPrime(n):
    # Time: O(sqrt(N) or N**0.5)
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return n > 1


def sieveOfEratosthenes(n):
    # Time: O(Nlog(logN))
    mark = [True] * (n + 1)
    primes = []
    mark[0] = mark[1] = False
    for i in range(2, int(n**0.5) + 1):
        if mark[i] == True:
            for j in range(i * i, n + 1, i):
                mark[j] = False
    for i in range(2, n + 1):
        if mark[i] == True:
            primes.append(i)
    return primes


n = 25
primes = sieveOfEratosthenes(n)
# for i in range(len(primes)):
#     print(primes[i], end=" ")
# print()


def segmentedSieve(left, right, primes):
    if left == 1:
        left += 1
    mark = [True] * (right - left + 1)
    i = 0
    while i < len(primes) and primes[i] <= right**0.5:
        base = left // primes[i] * primes[i]
        if base < left:
            base += primes[i]
        for j in range(base, right + 1, primes[i]):
            if j != primes[i]:
                mark[j - left] = False
        i += 1
    result = []
    for i in range(left, right + 1):
        if mark[i - left] == True:
            result.append(i)
    return result


left = 11
right = 34
primes = sieveOfEratosthenes(int(right**0.5))
result = segmentedSieve(left, right, primes)
# for p in result:
#     print(p, end=" ")
# print()

"""
Euler's totient function

phi -> phi(60) = 16 - a number of integers k in the range 1<=k<=n for which the gcd(n,k) = 1 (relatively prime)
Time: O(NlogN)

1. p is prime -> phi(p) = p - 1
2. p is prime and k >= 1: phi(p**k) = p**k - P**(k-1)
3. a,b are relatively prime <=> gcd(a,b) = 1: phi(a*b) = phi(a)*phi(b)

prime factorization
phi(n) = n*(1-1/p1)*(1-1/p2)*...*(1-1/pk)
Time: O(N**0.5)
"""


def gcd(a, b):
    while b != 0:
        remainder = a % b
        a = b
        b = remainder
    return a


def phi(n):
    # Time: O(NlogN)
    result = 1  # gcd(1, n)
    for i in range(2, n):
        if gcd(i, n) == 1:
            result += 1
    return result


n = 60
# print(f"Phi({n}) = {phi(n)}")


def improvedPhi(n):
    # Time: O(N**0.5)
    result = n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            while n % i == 0:
                n //= i
            result = result // i * (i - 1)
    if n > 1:
        result = result // n * (n - 1)
    return result


n = 60
# print(f"Improved Phi({n}) = {improvedPhi(n)}")

"""
Irreducible Basic Fractions

Example:
12
123456
7654321
0

4
41088
7251444
"""


def gcd(a, b):
    while b != 0:
        remainder = a % b
        a = b
        b = remainder
    return a


def phi(n):
    # Time: O(nlogn)
    result = 1
    for i in range(2, n):
        if gcd(i, n) == 1:
            result += 1
    return result


def improvedPhi(n):
    # Time: O(sqrt(n)) or O(n**0.5)
    result = n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            while n % i == 0:
                n //= i
            result = result // i * (i - 1)
    if n > 1:
        result = result // n * (n - 1)
    return result


def irreducibleBasicFractions():
    while True:
        n = int(input())
        if n == 0:
            break
        print(improvedPhi(n))
    return


irreducibleBasicFractions()


"""
Ana Prime
"""
MAX = 10**7
primes = [True] * (MAX + 1)
anaPrimes = []


def sieveOfEratosthenes():
    primes[0] = primes[1] = False
    for i in range(2, (MAX**0.5)):
        if primes[i] == True:
            for j in range(2, (MAX**0.5), i):
                primes[j] = False
                
def nextPermutation(a):
    # a: a list of digits
    m = len(a)
    for i in range(m-1, -1, -i):
        if a[i] < a[i+1]:
            for j in 
