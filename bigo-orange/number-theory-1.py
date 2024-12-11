"""
Number theory

Modular Arithmetic

(a**b)%m
"""


def modularExponentiation(a, b, m):
    result = 1
    for i in range(1, b + 1):
        result *= a
        result %= m
    return result


a = 50
b = 100
m = 13
# print(modularExponentiation(a, b, m))


def modularExponentiationImproved(a, b, m):
    result = 1
    a %= m
    while b > 0:
        # if b is odd, multiply a with result
        if b % 2 == 1:
            result = (result * a) % m
        # b must be even
        b //= 2
        a = (a * a) % m
    return result


a = 50
b = 100
m = 13
result = modularExponentiationImproved(a, b, m)
# print("Modular Exponentiation: ", a, " ^ ", b, " (mod ", m, ") = ", result, sep="")


def modularExponentiationBit(a, b, m):
    result = 1
    a %= m
    while b > 0:
        if b & 1:
            result = (result * a) % m
        b >>= 1
        a = (a * a) % m
    return result


result = modularExponentiationBit(a, b, m)
# print("Modular Exponentiation Bit: ", a, " ^ ", b, " (mod ", m, ") = ", result, sep="")


def modInverse(b, m):
    b = b % m
    for x in range(1, m):
        r = (b * x) % m
        if r == 1:
            return x
    return -1


b = 22
m = 17
# print(modInverse(b, m))


def modularExponentiationImproved(a, b, m):
    result = 1
    a %= m
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % m
        b //= 2
        a = (a * a) % m
    return result


def modInverse(b, m):
    res = modularExponentiationImproved(b, m - 2, m)
    if (res * b) % m == 1:
        return res
    return -1


b = 22
m = 17
# print(modInverse(b, m))


def gcd(a, b):
    while b != 0:
        remainder = a % b
        a = b
        b = remainder
    return a


def extendedEuclid(b, m):
    result = []
    x1 = 1
    y1 = 0
    x2 = 0
    y2 = 1
    x3 = 1
    y3 = 0
    while m != 0:
        q = b // m
        r = b % m
        x3 = x1 - q * x2
        y3 = y1 - q * y2
        x1 = x2
        y1 = y2
        x2 = x3
        y2 = y3
        b = m
        m = r
    result.append(b)
    result.append(x1)
    result.append(y1)
    return result


def modInverse(b, m):
    result = extendedEuclid(b, m)
    gcd = result[0]
    x = result[1]
    y = result[2]
    if gcd != 1:
        print("Inverse doesn't exist")
    else:
        print("Modular multiplicative inverse is:", (x + m) % m)


b = 19
m = 141
# modInverse(b, m)


"""
Drazil and his happy friends
"""


def drazilAndHappyFriends():
    # Time: O(n*m)
    n, m = map(int, input().split())
    boys = [0] * n
    girls = [0] * m
    d1 = list(map(int, input().split()))
    d2 = list(map(int, input().split()))
    b = d1[1:]
    g = d2[1:]
    for i in b:
        boys[i] = 1
    for i in g:
        girls[i] = 1
    for i in range(n * m):
        u = i % n
        v = i % m
        if boys[u] or girls[v]:
            boys[u] = 1
            girls[v] = 1
    happy_boy = 0
    happy_girl = 0
    for boy in boys:
        happy_boy += boy
    for girl in girls:
        happy_girl += girl
    if happy_boy == len(boys) and happy_girl == len(girls):
        print("Yes")
    else:
        print("No")
    return


# drazilAndHappyFriends()


def drazilSolution():
    # Time: O(n*m)
    n, m = map(int, input().split())
    men = [False] * n
    women = [False] * m
    d1 = list(map(int, input().split()))
    d2 = list(map(int, input().split()))
    x = d1[0]
    y = d2[0]
    mList = d1[1:]
    wList = d2[1:]
    for i in mList:
        men[i] = True
    for j in wList:
        women[j] = True
    for i in range(n * m):
        u = i % m
        v = i % n
        if men[u] or women[v]:
            men[u] = 1
            women[v] = 1
    for i in range(n):
        if men[i] == False:
            print("No")
            return
    for j in range(m):
        if women[j] == False:
            print("No")
            return
    print("Yes")


def improvedDrazil():
    n, m = map(int, input().split())
    d = gcd(n, m)
    A = [False] * d
    d1 = list(map(int, input().split()))
    d2 = list(map(int, input().split()))
    x = d1[0]
    y = d2[0]
    men = d1[1:]
    women = d2[1:]
    for i in men:
        A[i % d] = True
    for j in women:
        A[j % d] = True
    allHappy = True
    for i in range(d):
        if A[i] == False:
            allHappy = False
    print("Yes" if allHappy else "No")


# improvedDrazil()

"""
Problem Makes Problem

the problem is how many ways to make n by adding k non-negative integers
example:
n = 4, k = 3
considering a sequence of bit 1 -> 1 1 1 1
using k - 1 separator to separate the sequence such as 1 | 1 1 | 1 since k - 1 = 2
the bigger picture is that give a sequence of n + k - 1 bit 1 = 6 and a number separator is represented by bit 0
such as 1 0 1 1 0 1 

now the problem becomes count the number of ways to select k - 1 position to switch from 1 to 0 (separator) from
n + k - 1
"""


def modularExponentation(a, b, m):
    result = 1
    a = a % m
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % m
        b //= 2
        a = (a * a) % m
    return result


def modInverse(b, m):
    res = modularExponentation(b, m - 2, m)
    if (res * b) % m == 1:
        return res
    return -1


def problemMakesProblem():
    m = 10**9 + 7
    LIMIT = 10**6
    fact = [0] * (2 * LIMIT)
    fact[0] = 1
    for i in range(1, 2 * LIMIT):
        fact[i] = fact[i - 1] * i % m
    T = int(input())
    for tc in range(T):
        n, k = map(int, input().split())
        X = fact[k - 1] * fact[n] % m
        inverseX = modInverse(X, m)
        result = fact[n + k - 1] * inverseX % m
        print(f"Case {tc+1}: {result}")
        print()


# problemMakesProblem()

"""
Train Time Table

2
5
3 2
09:00 12:00
10:00 13:00
11:00 12:30
12:02 15:00
09:00 10:30
2
2 0
09:00 09:01
12:00 12:02
"""
import queue


class Train:
    def __init__(self, start, end, side):
        self.start = start
        self.end = end
        self.side = side  # side = 0 or 1 (A or B)

    def __lt__(self, other):
        return self.start < other.start


def trainTimeTable():
    N = int(input())
    for tc in range(N):
        T = int(input())
        NA, NB = map(int, input().split())
        a = []
        for i in range(NA):
            u, v = map(str, input().split())
            sH, sM = map(int, u.split(":"))
            eH, eM = map(int, v.split(":"))
            start = sH * 60 + sM
            end = eH * 60 + eM
            a.append(Train(start, end, 0))
        for i in range(NB):
            u, v = map(str, input().split())
            sH, sM = map(int, u.split(":"))
            eH, eM = map(int, v.split(":"))
            start = sH * 60 + sM
            end = eH * 60 + eM
            a.append(Train(start, end, 1))
        a.sort()  # sort a by start
        pq = [queue.PriorityQueue(), queue.PriorityQueue()]
        cnt = [0, 0]
        for i in range(NA + NB):
            x = a[i]
            # if pq[x.side].empty() or pq[x.side].queue[0] > x.start:
            #     cnt[x.side] += 1
            # else:
            #     pq[x.side].get()
            if not pq[x.side].empty() and pq[x.side].queue[0] <= x.start:
                pq[x.side].get()
            else:
                cnt[x.side] += 1
            pq[1 - x.side].put(x.end + T)
        print(f"Case #{tc+1}: {cnt[0]} {cnt[1]}")
        print()


trainTimeTable()
