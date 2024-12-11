"""
Lecture Note
"""

MAX = 100
V = None
E = None
visited = [False for i in range(MAX)]
path = [0 for i in range(MAX)]
graph = [[] for i in range(MAX)]


def DFS(src):
    s = []
    visited[src] = True
    s.append(src)
    while len(s) > 0:
        u = s.pop()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                s.append(v)
                path[v] = u


def DFSRecursion(s):
    visited[s] = True
    for v in graph[s]:
        if not visited[v]:
            path[v] = s
            DFSRecursion(v)


def printPath(s, f):
    ans = ""
    while f != s:
        ans += str(f) + ">-"
        f = path[f]
    ans += str(s)
    print(ans[::-1])
    return


if __name__ == "__main__":
    V, E = map(int, input().split())
    for i in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    s = 0
    f = 5
    for i in range(V):
        visited[i] = False
        path[i] = -1
    # DFSRecursion(s)
    DFS(s)
    printPath(s, f)

# 6 8
# 0 1
# 0 3
# 1 2
# 1 3
# 1 5
# 2 5
# 3 4
# 3 5

# 6 8
# 0 1
# 0 2
# 0 4
# 1 3
# 2 5
# 3 2
# 3 5
# 4 3

"""
Bomb Explosion
"""


from collections import deque


def bomb_explosion(source, n, m, graph, counter):
    # using BFS
    visisted = [False for _ in range(n + 1)]
    q = deque()
    visisted[source] = True
    q.append(source)
    while len(q):
        u = q.popleft()
        for v in graph[u]:
            if not visisted[v]:
                visisted[v] = True
                counter += 1
                q.append(v)

    return counter


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
explosion = [1 for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
for i in range(1, n + 1):
    explosion[i] = bomb_explosion(i, n, m, graph, counter=1)
print(max(explosion))


"""
Bishu and his girlfriends
"""
V = int(input())
MAX = V + 1
E = V - 1
visited = [False for i in range(MAX)]
path = [-1 for i in range(MAX)]
graph = [[] for i in range(MAX)]

for i in range(E):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dist = [0 for i in range(MAX)]


def DFS(src):
    s = []
    visited[src] = True
    s.append(src)
    while len(s) > 0:
        u = s.pop()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                s.append(v)
                path[v] = u
                dist[v] = dist[u] + 1


def bishu_and_girlfriends():
    src = 1
    DFS(src)
    ans = 0
    min_dist = V
    Q = int(input())
    for i in range(Q):
        u = int(input())
        if dist[u] < min_dist or (dist[u] == min_dist and u < ans):
            min_dist = dist[u]
            ans = u
    print(ans)
    return


bishu_and_girlfriends()

# 6
# 1 2
# 1 3
# 1 4
# 2 5
# 2 6
# 4
# 5
# 6
# 3
# 4

# 7
# 1 2
# 2 3
# 1 4
# 5 4
# 1 6
# 7 6
# 3
# 3
# 5
# 7


"""
Prayatna
"""


def DFS(src):
    s = [src]
    visited[src] = True
    while len(s) > 0:
        u = s.pop()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                path[v] = u
                s.append(v)
    return


# Tests
T = int(input())
for _ in range(T):
    V = int(input())  # vertices
    E = int(input())  # edges
    graph = [[] for _ in range(V)]
    visited = [False for _ in range(V)]
    path = [-1 for _ in range(V)]

    # Connecting edges
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    count = 0

    # run through each vertex, if that vertex is not visisted, add 1 to count then DFS that vertex to update visited list
    # because our purpose is to count the minimum person (vertex) to convey the message based on different circle group
    for i in range(V):
        if not visited[i]:
            count += 1
            DFS(i)

    print(count)


# 6
# 12
# 6
# 1 2
# 2 3
# 5 8
# 6 7
# 1 9
# 3 7
# 8
# 3
# 1 0
# 2 4
# 3 5
# 6
# 3
# 1 2
# 3 4
# 0 4
# 6
# 3
# 1 0
# 2 4
# 3 5
# 4
# 2
# 0 1
# 1 2
# 3
# 0

"""
Lakes in Berland
map: N x M
land: "*"
water: "."
k: # of lakes should be left on the map

output: 
print min number of cells needed to transform water to land
print updated map n x m
"""

N, M, k = map(int, input().split())
dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]
map = [None for _ in range(N)]
visited = [[False] * M for _ in range(N)]
lakes = []

for i in range(N):
    map[i] = list(input())


def on_edge(i, j):
    return i == 0 or j == 0 or i == N - 1 or j == M - 1


def is_valid(i, j):
    return i in range(N) and j in range(M)


def DFS(sr, sc):
    s = [(sr, sc)]
    visited[sr][sc] = True

    is_ocean = False
    temp = []

    while len(s) > 0:
        ur, uc = s.pop()
        temp.append((ur, uc))

        if on_edge(ur, uc):
            is_ocean = True

        for i in range(4):
            r = ur + dr[i]
            c = uc + dc[i]
            if is_valid(r, c) and map[r][c] == "." and not visited[r][c]:
                visited[r][c] = True
                s.append((r, c))

    if not is_ocean:
        lakes.append(temp)


for i in range(N):
    for j in range(M):
        if not visited[i][j] and map[i][j] == ".":
            DFS(i, j)

# for v in visited:
#     print(v)

# for lake in lakes:
#     print(lake)

lakes.sort(key=lambda lake: len(lake))
sum_cell = 0

for i in range(len(lakes) - k):
    sum_cell += len(lakes[i])
    for r, c in lakes[i]:
        map[r][c] = "*"

print(sum_cell)
for i in range(N):
    print("".join(map[i]))

# Test 1
# Input
# 5 4 1
# ****
# *..*
# ****
# **.*
# ..**

# Output
# 1
# ****
# *..*
# ****
# ****
# ..**

# Test 2
# Input
# 3 3 0
# ***
# *.*
# ***

# Output
# 1
# ***
# ***
# ***


"""
Dudu Service Maker
"""


import sys

sys.setrecursionlimit(10001)


def isCyclicUtil(u, graph, visited, recStack):
    # mark current node as visiited and add to recursion stack
    visited[u] = True
    recStack[u] = True

    # recur for all neighbors if any neighbor is visited and in recStack => graph is cyclic
    for v in graph[u]:
        if visited[v] == False:
            if isCyclicUtil(v, graph, visited, recStack) == True:
                return True
        elif recStack[v] == True:
            return True

    # node needs to be popped from recursion stack before function ends
    recStack[u] = False
    return False


def isCyclic(V):
    visited = [False] * (V + 1)
    recStack = [False] * (V + 1)
    for u in range(V):
        if visited[u] == False:
            if isCyclicUtil(u, graph, visited, recStack) == True:
                return True
    return False


T = int(input())
for _ in range(T):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)

    if isCyclic(V):
        print("YES")
    else:
        print("NO")

# 3
# 2 1
# 1 2
# 2 2
# 1 2
# 2 1
# 4 4
# 2 3
# 3 4
# 4 2
# 1 3


# Hướng dẫn
# Giải thích ví dụ:

# Gồm 3 đồ thị:

# Đồ thị 1 gồm 2 đỉnh và 1 cạnh (1, 2), không có cạnh từ 2 về 1 nên không tạo thành chu trình. Kết quả là NO.

# Đồ thị 2 gồm 2 đỉnh và 2 cạnh, tồn tại chu trình 1-2 nên kết quả là YES. Đồ thị 3 gồm 4 đỉnh và 4 cạnh, tồn tại chu trình 2-3-4 nên kết quả là YES.

# Hướng dẫn giải:

# Nhận xét: Đồ thị chỉ có thể tồn tại chu trình chỉ khi nào có một cạnh nối từ u đến một đỉnh v nào đó được thăm trước đó, đồng thời từ v phải đến được u.

# Do đó ta cần thêm một mảng để truy vết đường đi và kiểm tra điều kiện trên, tạm gọi là mảng path.

# Như vậy, ý tưởng giải cơ bản sẽ là sử dụng DFS để duyệt qua từng đỉnh, với mỗi đỉnh u đang xét, ta duyệt qua từng đỉnh v kề với u:

# Nếu v chưa thăm thì ta duyệt DFS(v).

# Nếu v thăm rồi, lúc này cần kiểm tra trong mảng path xem từ v có đến được u hay không, nếu đến được thì chứng tỏ có chu trình.

# Độ phức tạp: O(N) với mỗi đỉnh 🡪 O(
# 𝑁
# 2
# N
# ​2
# ​​ ) cho toàn đồ thị.

# Như vậy ta cần cải tiến để kiểm tra nhanh xem từ v có đến được u hay không.

# Nhận xét: Nếu từ v đến được u thì v sẽ nằm trên đường đi từ gốc DFS đến u. Như vậy, nếu mình đánh dấu lại các đỉnh thuộc đường đi từ gốc đến u, thì có thể kiểm tra nhanh v có thuộc đường đi đó hay không, đồng nghĩa với việc từ v có đến được u hay không.

# Do đó thay vì dùng mảng path, ta dùng một mảng là inPath với inPath[i] = true nếu i nằm trên đường đi từ gốc DFS đến đỉnh u đang xét, ngược lại inPath[i] = false.

# Khi mình duyệt xong DFS(u), thì lúc trở về đỉnh cha của u, chắc chắn u không nằm trên đường đi từ gốc đến cha của u, nên cần gán lại inPath[u] = false trước khi thoát khỏi DFS(u).

# Ngoài ra, còn một cách xử lý nữa là sử dụng mảng visited, nhưng thay vì lúc này chỉ đánh dấu 0/1 (false/true) thì lúc này mình đánh dấu 3 giá trị nhằm mục đích sử dụng nó để thực hiện chức năng của cả 2 mảng visited và path ở cách trên:

# visited[u] = 0 nếu u chưa được duyệt (tức visited[u] = false và inPath[u] = false theo cách vừa trình bày).

# visited[u] = 1 nếu u đã được duyệt và ta đang duyệt các đỉnh kề với u (visited[u] = true và inPath[u] = true).

# visited[u] = 2 nếu u đã được duyệt và đã duyệt xong các đỉnh kề với u (visited[u] = false và inPath[u] = false).

# Độ phức tạp: O(V + E) với V, E lần lượt là số lượng đỉnh và số lượng cạnh của đồ thị. Tuy nhiên, cách sử dụng mảng visited 3 giá trị sẽ ít tốn bộ nhớ hơn.


import sys

MAX = 10005
visited = [False] * MAX
graph = [[] for _ in range(MAX)]

sys.setrecursionlimit(MAX)


def DFS(u):
    visited[u] = 1
    for v in graph[u]:
        if visited[u] == 1:
            return True
        elif visited[u] == 0:
            if DFS(v):
                return True
    visited[u] = 2
    return False


T = int(input())
for _ in range(T):
    V, E = map(int, input().split())
    for i in range(V + 1):
        graph[i].clear()
        visited[i] = 0

    for i in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)

    isCyclic = False

    for i in range(1, V + 1):
        if visited[i] == 0:
            isCyclic = DFS(i)
            if isCyclic:
                break

    print("YES" if isCyclic else "NO")

# 3
# 2 1
# 1 2
# 2 2
# 1 2
# 2 1
# 4 4
# 2 3
# 3 4
# 4 2
# 1 3


"""
The Last Shot

Directed Graph
Find where to flash in order to get the maximum number of bombs exploded
"""


def DFS(src):
    count = 1
    visited = [False for _ in range(V + 1)]
    s = [src]
    visited[src] = True
    while len(s) > 0:
        u = s.pop()
        for v in graph[u]:
            if visited[v] == False:
                visited[v] = True
                count += 1
                s.append(v)

    return count


V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v = map(int, input().split())
    graph[u].append(v)

explosion = [0 for _ in range(V + 1)]
for i in range(1, V + 1):
    explosion[i] = DFS(i)
print(max(explosion))

"""
ALL IZZ WELL

T : # of tests
R,C: # of row col
"""
dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]
term = "ALLIZZWELL"


def is_valid(i, j):
    global N, M
    return i in range(N) and j in range(M)


def DFS(sr, sc, count):
    global found, visited, matrix
    if count == len(term):
        found = True
        return

    for i in range(8):
        r = sr + dr[i]
        c = sc + dc[i]
        if is_valid(r, c) and matrix[r][c] == term[count] and visited[r][c] == False:
            visited[r][c] = True
            DFS(r, c, count + 1)
            visited[r][c] = False


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    visited = [[False] * M for _ in range(N)]
    matrix = [None for _ in range(N)]

    for i in range(N):
        matrix[i] = input()

    found = False

    for i in range(N):
        for j in range(M):
            if matrix[i][j] == term[0] and not found:
                DFS(i, j, 1)

    print("YES" if found else "NO")
    input()

# 5
# 3 6
# AWE.QX
# LLL.EO
# IZZWLL

# 1 10
# ALLIZZWELL

# 2 9
# A.L.Z.E..
# .L.I.W.L.

# 3 3
# AEL
# LWZ
# LIZ

# 1 10
# LLEWZZILLA


"""
ABC Path
"""

dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]


def is_valid(i, j):
    global H, W
    return i in range(H) and j in range(W)


def DFS(sr, sc):
    global visited, matrix, dist

    for i in range(8):
        r = sr + dr[i]
        c = sc + dc[i]
        if (
            is_valid(r, c)
            and not visited[r][c]
            and matrix[r][c] == chr(ord(matrix[sr][sc]) + 1)
        ):
            visited[r][c] = True
            dist = max(dist, ord(matrix[r][c]) - ord("A") + 1)
            DFS(r, c)
            visited[r][c] = False


T = 1
while True:
    H, W = map(int, input().split())
    if H == 0 and W == 0:
        break
    visited = [[False] * W for _ in range(H)]
    matrix = [None for _ in range(H)]
    for i in range(H):
        matrix[i] = input()

    max_dist = 0

    for i in range(H):
        for j in range(W):
            if matrix[i][j] == "A" and not visited[i][j]:
                visited[i][j] = True
                dist = 1
                DFS(i, j)
                max_dist = max(max_dist, dist)
    print("Case " + str(T) + ": " + str(max_dist))
    T += 1

# Input
# 4 3
# ABE
# CFG
# BDH
# ABC
# 0 0

# Output
# Case 1: 4
