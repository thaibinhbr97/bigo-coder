from queue import Queue

MAX = 100
V = None  # vertices
E = None  # edges
visited = [False for i in range(MAX)]  # visited list
path = [0 for i in range(MAX)]  # path list
graph = [[] for i in range(MAX)]  # graph list of list


def BFS(s):
    for i in range(V):
        visited[i] = False
        path[i] = -1
    q = Queue()
    visited[s] = True
    q.put(s)
    while q.empty():
        u = q.get()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                q.put(v)
                path[v] = u


def printPath(s, f):
    b = []
    if f == s:
        print(s)
        return
    if path[f] == -1:
        print("No path")
        return
    while True:
        b.append(f)
        f = path[f]
        if f == s:
            b.append(s)
            break
    for i in range(len(b) - 1, -1, -1):
        print(b[i], end=" ")


def printPathRecursion(s, f):
    if s == f:
        print(f, end=" ")
    else:
        if path[f] == -1:
            print("No path")
        else:
            printPathRecursion(s, path[f])
            print(f, end=" ")


if __name__ == "__main__":
    V, E = map(int, input().split())
    for i in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    s = 0
    f = 5
    BFS(s)
    printPath(s, f)

"""
BFS: Shortest Reach 
n vertices from 1 to n
weight between vertices are always 6
s is a source of BFS
q queries
print a line including n - 1 separated by a "-" representing smallest distance to each n - 1 vertices (based on node number)
if there is no way from s to the other vertice, print -1 representing a distance to that other vertice.
"""


from queue import Queue


def bfs_shortest_reach(source, graph, visited, dist):
    visited[source] = True
    dist[source] = 0
    q = Queue()
    q.put(source)
    print(graph)
    while not q.empty():
        u = q.get()
        for ele in graph[u]:
            if not visited[ele]:
                visited[ele] = True
                q.put(ele)
                dist[ele] = dist[u] + 6
    ans = ""
    for k in range(1, len(dist)):
        if k != source:
            ans += str(dist[k]) + " "
    # ans.rstrip()
    print(ans)


queries = int(input())
for _ in range(queries):
    v, e = map(int, input().split())
    graph = [[] for l in range(v + 1)]  # graph list of list
    dist = [-1] * len(graph)
    visited = [False] * len(graph)  # visited list
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    source = int(input())
    bfs_shortest_reach(source, graph, visited, dist)


# 1 --- 2 ---- 4
# |
# 3


import queue

MAX = 1000 + 5
visited = [False] * MAX
dist = [0] * MAX
graph = [[] for i in range(MAX)]


def bfs_shortest_reach(s):
    q = queue.Queue()
    visited[s] = True
    q.put(s)

    while not q.empty():
        u = q.get()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                dist[v] = dist[u] + 1
                q.put(v)


Q = int(input())
for _ in range(Q):
    V, E = map(int, input().split())

    for i in range(MAX):
        graph[i].clear()
        visited[i] = False
        dist[i] = 0

    for i in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    s = int(input())
    bfs_shortest_reach(s)

    for i in range(1, V + 1):
        if i == s:
            continue

        print(dist[i] * 6 if visited[i] else -1, end=" ")
    print()


"""
Validate The Maze
1 entry and 1 exit and at least one path from entry to exit
for each maza -> valid or invalid

t: test cases
m n: rows columns
M: matrix
M[i][j] = # : wall
M[i][j] = . : space
"""
import queue

dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]
MAX = 21
visited = [[False] * MAX for _ in range(MAX)]
maze = [None] * MAX


class Cell:
    def __init__(self, r, c):
        self.r = r
        self.c = c


def is_valid(r, c):
    return r in range(m) and c in range(n)


def BFS(s, f):
    q = queue.Queue()
    q.put(s)
    visited[s.r][s.c] = True
    while not q.empty():
        u = q.get()
        if u.r == f.r and u.c == f.c:
            return True

        for i in range(4):
            r = u.r + dr[i]
            c = u.c + dc[i]
            if is_valid(r, c) and maze[r][c] == "." and not visited[r][c]:
                visited[r][c] = True
                q.put(Cell(r, c))
    return False


T = int(input())
for _ in range(T):
    m, n = map(int, input().split())
    for i in range(m):
        maze[i] = input()

    entrance = []
    for i in range(m):
        for j in range(n):
            visited[i][j] = False
            if maze[i][j] == "." and (i == 0 or j == 0 or i == m - 1 or j == n - 1):
                entrance.append(Cell(i, j))

    if len(entrance) != 2:
        print("invalid")
    else:
        s = entrance[0]
        f = entrance[1]
        if BFS(s, f):
            print("valid")
        else:
            print("invalid")


"""
Dhoom4
X: key
Y: new_new
now X will be (X*Y)%100000
each process takes 1 sec
output: min(time) to have result == value of the lock
"""

from collections import deque

MAX = 100000 + 5
MOD = 100000


def dhoom4(source, target, N, keys):
    # O(100000*N) for time
    dist = [-1] * MAX
    q = deque()
    q.append(source)
    dist[source] = 0

    while len(q):
        u = q.popleft()
        for key in keys:
            v = (u * key) % MOD

            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)

            if v == target:
                return dist[v]
    return -1


source, target = map(int, input().split())
N = int(input())
keys = list(map(int, input().split()))
print(dhoom4(source, target, N, keys))

source, target = 3, 30
N = 3
keys = [2, 5, 7]
print(dhoom4(source, target, N, keys))  # 2

source, target = 18363, 18838
N = 4
keys = [4571, 30338, 2123, 25466]
print(dhoom4(source, target, N, keys))  # 621


"""
kefa_and_park
n vertices
root = vertex 1 = Kefa's house
park has cats
requirement: avoid having m consecutive vertices with cats

output: count # of restaurants he can go without violating the requirement
"""
from collections import deque

MAX = 10**5 + 1

visited = [False] * MAX
graph = [[] for i in range(MAX)]
cat = [0] * MAX


def kefa_and_park(m):
    nRestaurants = 0
    visited[1] = True
    cat[1] = 1
    q = deque()
    q.append(1)
    while len(q):
        u = q.popleft()
        for v in graph[u]:
            if visited[v] == False:
                if A[v - 1] == 1:
                    cat[v] = cat[u] + 1
                # else:
                #     cat[v] = 0
                if cat[v] <= m:
                    if len(graph[v]) == 1:
                        nRestaurants += 1
                    else:
                        q.append(v)
    print(nRestaurants)
    return


n, m = map(int, input().split())
A = list(map(int, input().split()))
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
kefa_and_park(m)


from collections import deque


def kefa_and_park(m):
    visited[1] = True
    cat[1] = 1 if A[1] == 1 else 0
    q = deque()
    q.append(1)
    nRestaurant = 0
    while len(q) != 0:
        u = q.popleft()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                if A[v] == 1:
                    cat[v] = cat[u] + 1
                if cat[v] <= m:
                    if len(graph[v]) == 1:
                        nRestaurant += 1
                    else:
                        q.append(v)
    print(nRestaurant)
    return


n, m = map(int, input().split())
A = [None] + list(map(int, input().split()))
graph = [[] for i in range(n + 1)]
for _ in range(1, n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False for _ in range(n + 1)]
cat = [0 for _ in range(n + 1)]
kefa_and_park(m)


"""
.: space
#: fence
k: sheep
v: wolf
up down left right to access other 
"""


def sheep():
    return


"""
Guilty Prince
T: test cases
W,H: width, height
.: land
#: water
@: start
Output for each test case:
print a number of cell taken from the start
"""
import queue

MAX = 21
visited = [[False] * MAX for _ in range(MAX)]
maze = [None] * MAX
dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]


class Cell:
    def __init__(self, r, c):
        self.r = r
        self.c = c


def is_valid(r, c):
    return r in range(H) and c in range(W)


def BFS(s):
    q = queue.Queue()
    q.put(s)
    visited[s.r][s.c] = True
    count = 1
    while not q.empty():
        u = q.get()

        for i in range(4):
            r = u.r + dr[i]
            c = u.c + dc[i]
            if is_valid(r, c) and maze[r][c] == "." and not visited[r][c]:
                visited[r][c] = True
                q.put(Cell(r, c))
                count += 1
    return count


T = int(input())
for t in range(1, T + 1):
    W, H = map(int, input().split())

    for i in range(H):
        maze[i] = input()

    for i in range(H):
        for j in range(W):
            if maze[i][j] == "@":
                s = Cell(i, j)
            visited[i][j] = False
    ans = BFS(s)
    test = "Case " + str(t) + ":"
    print(test, ans)


"""
Slick
N: rows
M: cols
N,M <= 250
"""

MAX = 251
maze = [None] * MAX
slick = [0] * (MAX * MAX)
q = [None] * (MAX * MAX)

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]


class Cell:
    def __init__(self, r, c):
        self.r = r
        self.c = c


def is_valid(r, c):
    return r in range(N) and c in range(M) and maze[r][c] == "1"


def BFS(s):
    left = right = 0
    q[0] = s
    maze[s.r][s.c] = "0"
    count = 1

    while left <= right:
        ur = q[left].r
        uc = q[left].c
        left += 1

        for i in range(4):
            r = ur + dr[i]
            c = uc + dc[i]

            if is_valid(r, c):
                right += 1
                q[right] = Cell(r, c)
                maze[r][c] = "0"
                count += 1

    slick[count] += 1


while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break

    for i in range(N):
        maze[i] = input().split()
        for j in range(M):
            slick[i * M + j + 1] = 0

    nslicks = 0

    for i in range(N):
        for j in range(M):
            if maze[i][j] == "1":
                nslicks += 1
                BFS(Cell(i, j))

    print(nslicks)

    for i in range(1, N * M + 1):
        if slick[i]:
            print(i, slick[i], sep=" ")


"""
Ice Cave
n: rows
m: cols
.: normal
X: cracked
"""


MAX = 501
maze = [None] * MAX
q = [None] * (MAX * MAX)

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]


def is_valid(r, c):
    return r in range(n) and c in range(m) and maze[r][c] == "."


def BFS(sr, sc, fr, fc):
    left = right = 0
    q[0] = (sr, sc)
    maze[sr][sc] = "X"

    while left <= right:
        ur, uc = q[left]
        left += 1

        for i in range(4):
            r = ur + dr[i]
            c = uc + dc[i]

            if r == fr and c == fc and maze[r][c] == "X":
                return True

            if is_valid(r, c):
                maze[r][c] = "X"
                right += 1
                q[right] = (r, c)

    return False


n, m = map(int, input().split())

for i in range(n):
    maze[i] = list(input())

sr, sc = map(int, input().split())
fr, fc = map(int, input().split())

if BFS(sr - 1, sc - 1, fr - 1, fc - 1):
    print("YES")
else:
    print("NO")


"""
Sheep
#: fence
.: land
k: sheep
v: wolf

k > v => v die
k <= v => k die
k not in any area => k run and v stay => no one die

output: alive k and alive v
"""

dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

import queue


def is_valid(i, j):
    return i in range(N) and j in range(M)


def is_edge(i, j):
    return i == 0 or i == N - 1 or j == 0 or j == M - 1


def BFS(sr, sc):
    global survived_sheep, survived_wolf
    q = queue.Queue()
    q.put((sr, sc))
    visited[sr][sc] = True
    n_sheep = 0
    n_wolf = 0
    if land[sr][sc] == "k":
        n_sheep += 1
    elif land[sr][sc] == "v":
        n_wolf += 1
    outside = False
    while not q.empty():
        ur, uc = q.get()
        for i in range(4):
            r = ur + dr[i]
            c = uc + dc[i]
            if is_valid(r, c) and land[r][c] != "#" and visited[r][c] == False:
                visited[r][c] = True
                q.put((r, c))
                if land[r][c] == "k":
                    n_sheep += 1
                elif land[r][c] == "v":
                    n_wolf += 1
                if is_edge(r, c):
                    outside = True

    if outside == True:
        survived_sheep += n_sheep
        survived_wolf += n_wolf
    else:
        if n_sheep > n_wolf:
            survived_sheep += n_sheep
        else:
            survived_wolf += n_wolf

    return None


N, M = map(int, input().split())
visited = [[False] * M for _ in range(N)]
land = [None] * N
survived_sheep = 0
survived_wolf = 0

for i in range(N):
    land[i] = list(input())
for i in range(N):
    for j in range(M):
        if land[i][j] != "#" and visited[i][j] == False:
            BFS(i, j)

print(survived_sheep, survived_wolf)


# 8 8
# .######.
# #..k...#
# #.####.#
# #.#v.#.#
# #.#.k#k#
# #k.##..#
# #.v..v.#
# .######.

# 6 18
# .......k..v.......
# ...###############
# ....#.........#...
# ....#..v....k.#...
# ....#.........#...
# .....##########...


"""
Sheep
#: fence
.: land
k: sheep
v: wolf

k > v => v die
k <= v => k die
k not in any area => k run and v stay => no one die

N, M: rows, columns
next N row, input for each column

insight:
case 1 - wolf and sheep are on edge -> both wolf and sheep are alive since it can run away
case 2 - not on edge
    2.1 - if sheep > wolf -> wolf die, sheep alive
    2.2 - if wolf <= sheep -> wolf alive, sheep die

output: alive k and alive v in all cases
"""

import queue

dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]


def is_valid(i, j):
    return i in range(N) and j in range(M)


def is_edge(i, j):
    return i == 0 or j == 0 or i == N - 1 or j == M - 1


def BFS(sr, sc):
    # land[sr][sc] -> . k v -> freeland sheep wolf
    q = queue.Queue()
    visited[sr][sc] = True
    q.put((sr, sc))
    sheep = 0
    wolf = 0
    if land[sr][sc] == "k":
        sheep += 1
    elif land[sr][sc] == "v":
        wolf += 1
    outside = False
    while not q.empty():
        ur, uc = q.get()
        for i in range(4):
            r = ur + dr[i]
            c = uc + dc[i]
            if is_valid(r, c) and land[r][c] != "#" and visited[r][c] == False:
                visited[r][c] = True
                q.put((r, c))
                if land[r][c] == "k":
                    sheep += 1
                elif land[r][c] == "v":
                    wolf += 1
                if is_edge(r, c):
                    outside = True
    if outside == False:
        if sheep > wolf:
            wolf = 0
        elif sheep <= wolf:
            sheep = 0

    return sheep, wolf


N, M = map(int, input().split())
land = [None] * N
visited = [[False] * M for _ in range(N)]
surv_sheep = 0
surv_wolf = 0
for i in range(N):
    land[i] = list(input())
for i in range(N):
    for j in range(M):
        if land[i][j] != "#" and visited[i][j] == False:
            sheep, wolf = BFS(i, j)
            surv_sheep += sheep
            surv_wolf += wolf

print(surv_sheep, surv_wolf)


import queue

dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

N, M = map(int, input().split())
land = [None] * N
s_sheep = 0
s_wolf = 0


def is_valid(i, j):
    return i in range(N) and j in range(M)


def BFS(sr, sc):
    q = queue.Queue()
    sheep = 1 if land[sr][sc] == "k" else 0
    wolf = 1 if land[sr][sc] == "v" else 0
    land[sr][sc] = "#"
    can_escape = False
    q.put((sr, sc))
    while not q.empty():
        ur, uc = q.get()
        for i in range(4):
            r = ur + dr[i]
            c = uc + dc[i]

            if not is_valid(r, c):
                can_escape = True
                continue

            if land[r][c] != "#":
                sheep += 1 if land[r][c] == "k" else 0
                wolf += 1 if land[r][c] == "v" else 0
                land[r][c] = "#"
                q.put((r, c))

    if not can_escape:
        if sheep > wolf:
            wolf = 0
        else:
            sheep = 0
    return sheep, wolf


for i in range(N):
    land[i] = list(input())
for i in range(N):
    for j in range(M):
        if land[i][j] != "#":
            sheep, wolf = BFS(i, j)
            s_sheep += sheep
            s_wolf += wolf

print(s_sheep, s_wolf)
