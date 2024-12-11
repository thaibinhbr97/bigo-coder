"""
Lecture Note
Disjoint Set Union (DSU)
Alternative: Disjoint-Set, Union-Find

makeSet(): create a set for each initial element
findSet(u): find a root parent of a set containing u
unionSet(u,v): combine a set containing u and a set containing v
to a bigger set. If element u and element v belongs to the same set
this operation will not change anything

Time: O(N)

u v 1: union(u,v) -> unionSet(u,v)
u v 2: find(u) -> check if u,v has connections or belongs to the
same root parent or not

if u v 2 -> print whether u and v has connections or not.
YES if it does and NO otherwise
"""

MAX = 20
parent = []


def makeSet():
    global parent
    parent = [i for i in range(MAX + 5)]


def findSet(u):
    while u != parent[u]:
        u = parent[u]
    return u


def unionSet(u, v):
    up = findSet(u)
    vp = findSet(v)
    parent[up] = vp


if __name__ == "__main__":
    Q = int(input())
    makeSet()
    for i in range(Q):
        u, v, q = map(int, input().split())
        if q == 1:
            unionSet(u, v)
        if q == 2:
            parentU = findSet(u)
            parentV = findSet(v)
            if parentU == parentV:
                print("YES")
            else:
                print("NO")


"""
Union by rank and path compression -> optimization to find path to root parent node faster
O(logN)

having another list called ranks to keep track which node has a higher rank and it will be a root parent node
"""


MAX = 20
parent = []
ranks = []


def makeSet():
    global parent, ranks
    parent = [i for i in range(MAX + 5)]
    ranks = [0 for i in range(MAX + 5)]


# Path Compression
def findSet(u):
    if parent[u] != u:
        parent[u] = findSet(parent[u])
    return parent[u]


# Union By Rank
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


if __name__ == "__main__":
    Q = int(input())
    makeSet()
    for i in range(Q):
        u, v, q = map(int, input().split())
        if q == 1:
            unionSet(u, v)
        if q == 2:
            parentU = findSet(u)
            parentV = findSet(v)
            if parentU == parentV:
                print("YES")
            else:
                print("NO")

"""
Friends

N residents
A B: friend
B C: friend
=> A C: also friend

input
N,M: # of residents and # of pairs
"""


def makeSet(N):
    parent = [i for i in range(N + 1)]
    return parent


def findSet(u):
    if parent[u] != u:
        parent[u] = findSet(parent[u])
    return parent[u]


def unionSet(u, v):
    up = findSet(u)
    vp = findSet(v)
    if up == vp:
        return
    if ranks[up] < ranks[vp]:
        ranks[up] += ranks[vp]
        ranks[vp] = up
        parent[vp] = up
    elif ranks[up] > ranks[vp]:
        ranks[vp] += ranks[up]
        ranks[up] = vp
        parent[up] = vp
    else:
        ranks[up] += ranks[vp]
        ranks[vp] = up
        parent[vp] = up


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    parent = makeSet(N)
    ranks = [-1 for _ in range(N + 1)]
    for _ in range(M):
        u, v = map(int, input().split())
        unionSet(u, v)
    print(abs(min(ranks)))

# input
# 1
# 3 2
# 1 2
# 2 3
# output
# 3

# input
# 1
# 10 12
# 1 2
# 3 1
# 3 4
# 5 4
# 3 5
# 4 6
# 5 2
# 2 1
# 7 1
# 1 2
# 9 10
# 8 9
# output
# 7


"""
Graph Connectivity

G is connected when it exists a direct path between any vertices in G

maximum connected subgraph exists if no vertex and edge in the orginal graph can be added to subgraph and still leave it connected
example {A,B,D} and {C,E}

output:
determine # of maximum connected subgraph given a graph
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
    if ranks[up] < ranks[vp]:
        ranks[up] += ranks[vp]
        ranks[vp] = up
        parent[vp] = up
    elif ranks[up] > ranks[vp]:
        ranks[vp] += ranks[up]
        ranks[up] = vp
        parent[up] = vp
    else:
        ranks[up] += ranks[vp]
        ranks[vp] = up
        parent[vp] = up


T = int(input())
input()
for _ in range(T):
    end = input()
    N = ord(end) - ord("A")
    parent = [i for i in range(N + 1)]
    ranks = [-1 for i in range(N + 1)]
    while True:
        try:
            data = input()
            if data == "":
                break
            if len(data) == 2:
                u = ord(data[0]) - ord("A")
                v = ord(data[1]) - ord("A")
                unionSet(u, v)
        except EOFError:
            break
    ans = 0
    for rank in ranks:
        if rank < 0:
            ans += 1
    print(ans)
    print()

# input
# 2

# E
# AB
# BC
# CD
# EA

# output
# 2


"""
Forests

T: # of trees
P: # of people

input
tc: test cases
blank line
ith tc description
blank line

each tc
P T
i j: a person ith witness a tree jth falled

output
ans: how many different opinions are there?
same opinion occurs when they observe the same set of tree falled
blank line
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


Q = int(input())
input()
while Q > 0:
    P, T = map(int, input().split())
    parent = [i for i in range(P + 1)]
    ranks = [0 for i in range(P + 1)]
    witness = [set() for i in range(P + 1)]

    while True:
        try:
            line = input()
            if not line:
                break
            person, tree = map(int, line.split())
            witness[person].add(tree)
        except EOFError:
            break

    # union a person witnessed a set of trees that falled with a person witnessed the same thing
    # then we can count how many sets are there after union which also means the result representing
    # different opinions from the input
    for i in range(1, P + 1):
        for j in range(i, P + 1):
            if witness[i] == witness[j]:
                unionSet(i, j)

    # use parent to check how many different sets are they
    count = 0
    for i in range(1, P + 1):
        if i == parent[i]:
            count += 1
    print(count)

    Q -= 1
    print()


# input
# 2

# 1 20
# 1 1
# 1 2
# 1 3
# 1 4
# 1 5
# 1 6
# 1 7
# 1 8
# 1 9
# 1 10
# 1 11
# 1 12
# 1 13
# 1 14
# 1 15
# 1 16
# 1 17
# 1 18
# 1 19
# 1 20

# 20 1
# 1 1
# 2 1
# 3 1
# 4 1
# 5 1
# 6 1
# 7 1
# 8 1
# 9 1
# 10 1
# 11 1
# 12 1
# 13 1
# 14 1
# 15 1
# 16 1
# 17 1
# 18 1
# 19 1
# 20 1

# output
# 1

# 1


"""
Lost and Survived
"""

import queue


def findSet(u):
    if parent[u] != u:
        parent[u] = findSet(parent[u])
    return parent[u]


def unionSet(u, v):
    up, vp = findSet(u), findSet(v)
    if up == vp:
        return
    if ranks[up] > ranks[vp]:
        parent[vp] = up
        nums[up] += nums[vp]
        return (nums[up], up)
    elif ranks[up] < ranks[vp]:
        parent[up] = vp
        nums[vp] += nums[up]
        return (nums[vp], vp)
    else:
        parent[up] = vp
        nums[vp] += nums[up]
        ranks[vp] += 1
        return (nums[vp], vp)


N, Q = int(input())
Max = 1
Min = 1
parent = [i for i in range(N + 1)]
nums = [1 for i in range(N + 1)]
pq = queue.PriorityQueue()


for i in range(Q):
    u, v = map(int, input().split())
    p, num = unionSet(u, v)
    Max = max(Max, p)
    pq.put(Max, nums[Max])
    while parent[pq.get()[1]] != pq.get()[1] or nums[pq.get()[1]] != pq.get()[0]:
        pq.pop()
    Min = pq.get()[0]
    print(Max - Min)


"""
War

if two people are in the same set -> they are friend, otherwise enemy
Having two ranges:
I: [0, MAX) -> friend
II: [MAX, 2*MAX -1] -> enemy
~ : friend
* : enemy
for each x, if x is in I and x + MAX is in II -> x * (x+MAX)
1. setFriends(x,y)
x ~ y
x * (x+MAX) -> y * (x+MAX)
y * (y+MAX) -> (x+MAX) ~ (y+MAX)
unionSet(x,y) and unionSet(x+MAX,y+MAX)
2. setEnemies(x,y)
x * y
x * (x+MAX) -> (x+MAX) ~ y
y * (y+MAX) -> x ~ (y+MAX)
unionSet(x+MAX, y) and unionSet(x,y+MAX)
3. areFriends(x,y)
findSet(x) == findSet(y)
4. areEnemies(x,y)
areFriends(x,y+MAX) == True
"""

MAX = 10000


def findSet(u):
    # Path Compression
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


def areFriends(u, v):
    return findSet(u) == findSet(v)


def areEnemies(u, v):
    # return findSet(u) == findSet(v + MAX)
    return areFriends(u, v + MAX)


N = int(input())
parent = [i for i in range(2 * MAX)]
ranks = [0 for i in range(2 * MAX)]
while True:
    command, u, v = map(int, input().split())
    if command == 0 and u == 0 and v == 0:
        break
    if command == 1:
        if areEnemies(u, v):
            print("-1")
        else:
            unionSet(u, v)
            unionSet(u + MAX, v + MAX)
    elif command == 2:
        if areFriends(u, v):
            print("-1")
        else:
            unionSet(u, v + MAX)
            unionSet(u + MAX, v)
    elif command == 3:
        if areFriends(u, v):
            print("1")
        else:
            print("0")
    elif command == 4:
        if areEnemies(u, v):
            print("1")
        else:
            print("0")


# input
# 10
# 1 0 1
# 1 1 2
# 2 0 5
# 3 0 2
# 3 8 9
# 4 1 5
# 4 1 2
# 4 8 9
# 1 8 9
# 1 5 2
# 3 5 2
# 0 0 0

"""
Ice Skating

input:
n: # of snow drifts
xi yi: coordinate of snow drift ith

output:
print a number of snow drift needed to move from one to another snow drifts
"""


class Snow:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def isSameSet(self, other):
        # can move from one to another snow drifts
        return self.x == other.x or self.y == other.y


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


# Time: O(M*log(N)), N is # of input and M is a connection between points
n = int(input())
parent = [i for i in range(n)]
ranks = [0 for i in range(n)]
drifts = []
for i in range(n):
    x, y = map(int, input().split())
    drift = Snow(x, y)
    drifts.append(drift)
    for j in range(i):
        # if drift i and drift can move to each other's places, they are in the same set, so we can union them
        if drifts[j].isSameSet(drifts[i]):
            unionSet(i, j)
ans = 0
for i in range(n):
    if i == parent[i]:
        ans += 1
print(ans - 1)

"""
Cthulhu
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


N, M = map(int, input().split())
parent = [i for i in range(N + 1)]
ranks = [0 for i in range(N + 1)]


def solve():
    # O(N*log(M)), N is # of vertices, M is # of edges
    if N != M:
        print("NO")
        return
    for i in range(M):
        u, v = map(int, input().split())
        unionSet(u, v)

    res = 0
    for i in range(1, N + 1):
        if parent[i] == i:
            res += 1
            if res > 1:
                break
    if res == 1:
        print("FHTAGN!")
    else:
        print("NO")
    return


solve()

"""
Lost and Survived

input:
N, Q: # of survivors, # of queries
each query: A B: A and B becomes a bigger group

output:
print a difference between max group and min group after each query

example:
5 3
1 2
2 3
5 4

1
2
1
"""
import queue


def max(a, b):
    if a > b:
        return a
    return b


def findSet(u):
    if parent[u] != u:
        parent[u] = findSet(parent[u])
    return parent[u]


maxi = 0


def unionSet(u, v):
    up = findSet(u)
    vp = findSet(v)

    if up != vp:
        count[up] += count[vp]
        parent[vp] = up
        pq.put((count[up], up))
    return count[up]


pq = queue.PriorityQueue()

N, Q = map(int, input().split())
parent = [0 for i in range(N + 1)]
count = [0 for i in range(N + 1)]

for i in range(1, N + 1):
    count[i] = 1
    parent[i] = i
    pq.put((1, i))

for i in range(Q):
    u, v = map(int, input().split())
    maxi = max(maxi, unionSet(u, v))
    while True:
        temp = pq.queue[0]
        up = findSet(temp[1])
        if up != temp[1]:
            pq.get()
            continue

        if count[up] != temp[0]:
            pq.get()
            continue

        break
    mini = pq.queue[0][0]
    print(maxi - mini)

"""
Two sets


"""
n, a, b = map(int, input().split())
p = list(map(int, input().split()))

print(p)


# 4 5 9
# 2 3 4 5


# YES
# 0 0 1 1
