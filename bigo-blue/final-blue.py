"""
MUH and Important Things

input
n: # of quests
h ith: difficulty of quest ith
"""


def printSol(A):
    for val in A:
        print(val[1], end=" ")


def problem1():
    n = int(input())
    nums = list(map(int, input().split()))
    A = []
    for i, num in enumerate(nums):
        A.append((num, i + 1))
    A.sort()
    # print(A)
    swaps = []
    for i in range(1, len(A)):
        if A[i][0] == A[i - 1][0]:
            swaps.append((i, i - 1))
    if len(swaps) < 2:
        print("NO")
        return
    print("YES")
    printSol(A)
    print()
    first = swaps[0]
    A[first[0]], A[first[1]] = A[first[1]], A[first[0]]
    printSol(A)
    print()
    second = swaps[1]
    A[second[0]], A[second[1]] = A[second[1]], A[second[0]]
    printSol(A)
    print()
    return


problem1()

"""
Fibsieve Fantabulous
"""

from math import ceil


def ans(n):
    area = ceil(n**0.5)
    high = area**2
    mid = high - area + 1
    r = min(high - n + 1, area)
    c = min(n - mid + area, area)
    if area & 1:
        return (r, c)
    return (c, r)


T = int(input())
for t in range(1, T + 1):
    n = int(input())
    c, r = ans(n)
    print("Case %d: %d %d" % (t, c, r))


"""
Ubiquitous Religions
"""


def findSet(u):
    if parent[u] != u:
        parent[u] = findSet(parent[u])
    return parent[u]


def unionSet(u, v):
    up = findSet(u)
    vp = findSet(v)
    if up == vp:
        return
    if ranks[up] > ranks[vp]:
        parent[vp] = up
    elif ranks[up] < ranks[vp]:
        parent[up] = vp
    else:
        parent[up] = vp
        ranks[vp] += 1


t = 1
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    parent = [i for i in range(n + 1)]
    ranks = [0 for i in range(n + 1)]
    for i in range(m):
        u, v = map(int, input().split())
        unionSet(u, v)
    ans = 0
    for i in range(1, n + 1):
        if i == parent[i]:
            ans += 1
    print("Case " + str(t) + ": " + str(ans))
    t += 1


"""
Freckles
"""

# t = int(input())
# input()
# for i in range(t):
#     n = int(input())

"""
Phone List
"""


class Node:
    def __init__(self):
        self.countWord = 0
        self.child = dict()


def isConsistent(root, s):
    temp = root
    for ch in s:
        if ch not in temp.child:
            temp.child[ch] = Node()
        temp = temp.child[ch]
        if temp.countWord != 0:
            return True
    temp.countWord += 1
    if temp.child:
        return True
    return False


T = int(input())
for _ in range(T):
    n = int(input())
    root = Node()
    printed = False
    for i in range(n):
        s = input()
        if isConsistent(root, s) and not printed:
            printed = True
            print("NO")
            break
    if not printed:
        print("YES")
