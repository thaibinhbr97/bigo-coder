"""
Lecture Note

Minimum Spanning Tree (MST)
application: networking or public tranportation system

Using adjacent matrix
Time Complexity: O(V^2) or (V^2+E)

Using Priority Queue
Time Complexity: O(Elog(V))

Idea:
1. starting from any vertice -> go to adjacent vertices
2. compare cost of current edge to cost of previous edge
3. if it is smaller -> add priority queue, mark this as a new cost for the vertice
, and mark this vertice connected to the previous vertice
4. get the new vertice from priority queue (with the smallest cost)
5. stop when there is no vertice in priority queue
6. print the result
"""

import queue

INF = 1e9


class Node:
    def __init__(self, id, dist):
        self.id = id
        self.dist = dist

    def __lt__(self, other):
        return self.dist <= other.dist


def printMST():
    ans = 0
    for i in range(n):
        if path[i] == -1:
            continue
        ans += dist[i]
        print(f"{path[i]} - {i}: {dist[i]}")
    print(f"Weight of MST: {ans}")


def prim(src):
    pq = queue.PriorityQueue()
    pq.put(Node(src, 0))
    dist[src] = 0
    while pq.empty() == False:
        top = pq.get()
        u = top.id
        w = top.dist
        if dist[u] != w:
            continue
        visited[u] = True
        for neighbor in graph[u]:
            v = neighbor.id
            v_weight = neighbor.dist
            if visited[v] == False and v_weight < dist[v]:
                dist[v] = v_weight
                pq.put(Node(v, v_weight))
                path[v] = u


if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [[] for i in range(n)]
    dist = [INF for i in range(n)]
    path = [-1 for i in range(n)]
    visited = [False for i in range(n)]
    for i in range(m):
        u, v, w = map(int, input().split())
        graph[u].append(Node(v, w))
        graph[v].append(Node(u, w))
    prim(0)
    printMST()

"""
Minimum Spanning Tree
N,M: vertices, edges
i,j,k: i->j and j->i with k weight

Output:
Total weight for the minimum spanning tree
"""

import queue


class Node:
    def __init__(self, id, dist):
        self.id = id
        self.dist = dist

    def __lt__(self, other):
        return self.dist <= other.dist


INF = float("inf")
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
path = [-1 for _ in range(N + 1)]
dist = [INF for _ in range(N + 1)]


def prim(src):
    pq = queue.PriorityQueue()
    pq.put(Node(src, 0))
    dist[src] = 0
    while pq.empty() == False:
        top = pq.get()
        u = top.id
        u_weight = top.dist
        if dist[u] != u_weight:
            continue
        visited[u] = True
        for neighbor in graph[u]:
            v = neighbor.id
            w = neighbor.dist
            if visited[v] == False and w < dist[v]:
                dist[v] = w
                pq.put(Node(v, w))
                path[v] = u


def printMST():
    # using path
    ans = 0
    for i in range(N + 1):
        if path[i] == -1:
            continue
        ans += dist[i]
        # print(f"{path[i]} - {i}: {dist[i]}")
    # print(f"Weight of MST: {ans}")
    print(ans)

    # # using visited
    # ans = 0
    # for i in range(1, N + 1):
    #     if visited[i] == True:
    #         ans += dist[i]
    # print(ans)


for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append(Node(v, w))
    graph[v].append(Node(u, w))
prim(1)
printMST()


# 4 5
# 1 2 10
# 2 3 15
# 1 3 5
# 4 2 2
# 4 3 40


"""
Connect the Campus

each building is a point by (x,y)

Input
N
each N
M
each M

Example:
Input
4
103 104
104 100
104 103
100 100
1
4 2

Output
4.41
"""

import math
import queue

INF = float("inf")


class Node:
    def __init__(self, id, dist):
        self.id = id
        self.dist = dist

    def __lt__(self, other):
        return self.dist <= other.dist


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distanceTo(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


def prim(src, dist, graph, visited, path):
    pq = queue.PriorityQueue()
    pq.put(Node(src, 0))
    dist[src] = 0
    while pq.empty() == False:
        top = pq.get()
        u = top.id
        u_weight = top.dist
        if dist[u] != u_weight:
            continue
        visited[u] = True
        for neighbor in graph[u]:
            v = neighbor.id
            w = neighbor.dist
            if visited[v] == False and w < dist[v]:
                dist[v] = w
                pq.put(Node(v, w))
                path[v] = u


def printMST(N, path, dist):
    ans = 0
    for i in range(N + 1):
        if path[i] == -1:
            continue
        ans += dist[i]
        # print(f"{path[i]} - {i}: {dist[i]}")
    # print(f"Total length of cable: {ans:.2f}")
    print(f"{ans:.2f}")


def solve():
    N = int(input())
    buildings = dict()
    dist = [INF for _ in range(N + 1)]
    visited = [False for _ in range(N + 1)]
    graph = [[] for _ in range(N + 1)]
    path = [-1 for i in range(N + 1)]

    for i in range(1, N + 1):
        x, y = map(int, input().split())
        buildings[i] = Coordinate(x, y)

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i != j:
                building_i = buildings[i]  # Coordinate
                building_j = buildings[j]  # Coordinate
                distance = building_i.distanceTo(building_j)
                graph[i].append(Node(j, distance))

    M = int(input())

    for _ in range(M):
        i, j = map(int, input().split())
        graph[i].append(Node(j, 0))
        graph[j].append(Node(i, 0))

    prim(1, dist, graph, visited, path)
    printMST(N, path, dist)


while True:
    try:
        solve()
    except EOFError:
        break

"""
Cobbled Streets

Input
t: test cases
p: price to pave a street
n: # of main buildings in town
m: # of streets in town
a b c: building a has a street to building b with distance c

Output
for each test case, print a minimum cost to pave streets in which
all buildings are conneted
"""
import queue

INF = float("inf")


class Node:
    def __init__(self, id, dist):
        self.id = id
        self.dist = dist

    def __lt__(self, other):
        return self.dist <= other.dist


def prim(src):
    pq = queue.PriorityQueue()
    pq.put(Node(src, 0))
    dist[src] = 0
    while pq.empty() == False:
        top = pq.get()
        u = top.id
        u_weight = top.dist
        if dist[u] != u_weight:
            continue
        visited[u] = True
        for neighbor in graph[u]:
            v = neighbor.id
            w = neighbor.dist
            if visited[v] == False and w < dist[v]:
                dist[v] = w
                pq.put(Node(v, w))
                path[v] = u


def minCostPavement(p):
    ans = 0
    for i in range(n + 1):
        if path[i] == -1:
            continue
        ans += dist[i] * p
    print(ans)


T = int(input())

for _ in range(T):
    p = int(input())  # price to pave a street
    n = int(input())
    m = int(input())

    graph = [[] for _ in range(n + 1)]
    dist = [INF for _ in range(n + 1)]
    path = [-1 for _ in range(n + 1)]
    visited = [False for _ in range(n + 1)]

    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append(Node(v, w))
        graph[v].append(Node(u, w))

    prim(1)
    minCostPavement(p)


"""
Road Construction

undirected graph for cities
some streets are damaged and cannot be used
objective is to rebuild these broken streets to have a way between all cities

input:
broken streets -> city1 city2 cost
stable streets -> city1 city2 0

input:
T: test cases
: space
m: # of streets
each m line: city1 city2 cost/0

output:
case i: ans
"""
import queue

INF = float("inf")
MAX = 51


class Node:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    def __lt__(self, other):
        return self.cost <= other.cost


T = int(input())
for t in range(1, T + 1):
    input()
    m = int(input())
    graph = {}  # {name: [Node(name, cost),...], ...}
    # graph = [[] for _ in range(MAX)]
    for i in range(m):
        u, v, w = map(str, input().split())
        if u in graph:
            graph[u].append(Node(v, w))
        else:
            graph[u] = []
        if v in graph:
            graph[v].append(Node(u, w))
        else:
            graph[v] = []
    N = len(graph)
    dist = {}  # {name: cost, ...}
    visited = [False for _ in range(MAX)]
    path = {}  # {name: name, ...}
