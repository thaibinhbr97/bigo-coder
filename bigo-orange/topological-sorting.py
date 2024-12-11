"""
Topological Sort is based on DFS. There are many possibilities for Directed Acyclic Graph (DAG). 
2 algos to solve topo sort:
- Algo based on DFS
- Algo based on BFS (Kahn algo)
Time Complex: O(V+E)

DFS based
graph: adjacency list
visited: visited list
result: list => later reverse result to get answer

BFS based (Kahn algo)
graph: adjacency list
indegree: degree list
zero_indegree: queue that has a 0 degree node/vertex
result: list
"""

"""
Code for Topo Sort using DFS

input:
8 9
0 1
1 2
1 5
1 6
4 1
4 7
7 6
3 7
3 5
"""


# Using DFS:
# def dfs(u, graph, visited, result):
#     visited[u] = True
#     for v in graph[u]:
#         if not visited[v]:
#             dfs(v, graph, visited, result)
#     result.append(u)


# def topologicalSort(graph, result):
#     visited = [False] * V
#     for i in range(V):
#         if not visited[i]:
#             dfs(i, graph, visited, result)
#     result.reverse()


# if __name__ == "__main__":
#     V, E = map(int, input().split())
#     graph = [[] for i in range(V)]
#     result = []
#     for i in range(E):
#         u, v = map(int, input().split())
#         graph[u].append(v)
#     topologicalSort(graph, result)
#     print("Topological Sort of graph:")
#     for i in range(V):
#         print(result[i], end=" ")

# Using BFS (Kahn algo)


# import queue


# def topologicalSort(graph, result):
#     indegree = [0] * V
#     zero_indegree = queue.Queue()
#     for u in range(V):
#         for v in graph[u]:
#             indegree[v] += 1
#     for i in range(V):
#         if indegree[i] == 0:
#             zero_indegree.put(i)
#     while not zero_indegree.empty():
#         u = zero_indegree.get()
#         result.append(u)
#         for v in graph[u]:
#             indegree[v] -= 1
#             if indegree[v] == 0:
#                 zero_indegree.put(v)
#     return len(result) == V


# if __name__ == "__main__":
#     V, E = map(int, input().split())
#     graph = [[] for i in range(V)]
#     result = []
#     for i in range(E):
#         u, v = map(int, input().split())
#         graph[u].append(v)
#     if topologicalSort(graph, result):
#         print("Topological Sort of graph:")
#         for i in range(V):
#             print(result[i], end=" ")
#     else:
#         print("No result")


"""
Topological Sorting

obj: 
need to print all duties in correct order

input:
n, m: # of jobs, # of connections
next m: job x needs to be done before job y

output:
Sandro fails. -> if all duties cannot be completed on the list
correct order -> if possible
if multiple solutions exist, print smallest first

example 1:
8 9
1 4
1 2
4 2
4 3
3 2
5 2
3 5
8 2
8 6

1 4 3 5 7 8 2 6 

example 2:
2 2
1 2
2 1

Sandro fails.
"""
# Using Kahn algo (BFS) and min heap
import queue


def topoSort(graph, indegree):
    zero_indegree = queue.PriorityQueue()
    result = []
    for i in range(V):
        if indegree[i] == 0:
            zero_indegree.put(i)
    while not zero_indegree.empty():
        u = zero_indegree.get()
        result.append(u)
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                zero_indegree.put(v)
    return result


def solveTopoSort():
    global V, E
    V, E = map(int, input().split())
    graph = [[] for _ in range(V)]
    indegree = [0 for _ in range(V)]
    for i in range(E):
        u, v = map(int, input().split())
        graph[u - 1].append(v - 1)
        indegree[v - 1] += 1
    result = topoSort(graph, indegree)
    if len(result) < V:
        print("Sandro fails.")
        return
    for i in range(V):
        print(result[i] + 1, end=" ")


# solveTopoSort()


# Using DFS (not working)


def dfs(u, graph, visited, result):
    visited[u] = True
    for v in graph[u]:
        if not visited[v]:
            dfs(v, graph, visited, result)
    result.append(u)


def topologicalSort(V, graph, result):
    visited = [False] * (V + 1)
    for i in range(1, V + 1):
        if not visited[i]:
            dfs(i, graph, visited, result)
    result.reverse()


def solveTopologicalSorting():
    V, E = map(int, input().split())
    graph = [[] for i in range(V + 1)]
    result = []

    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
    topologicalSort(V, graph, result)
    if len(result) == V:
        for i in range(V):
            print(result[i], end=" ")
    else:
        print("Sandro fails.")


# solveTopologicalSorting()


"""
Hierarchy

N, K: total students, number of successful students
K lines
Ath: W wishes, W integers from [1,N] which student A wants to be superior to

Example 1:
4 2
1 3
2 3 4

4
0
1
2

Example 2:
7 4
2 2 3
1 6
1 7
2 1 2

4
7
1
5
0
2
3
"""
from queue import Queue


def topoSort(N, graph):
    indegree = [0 for i in range(N + 1)]
    for u in range(1, N + 1):
        for v in graph[u]:
            indegree[v] += 1
    queue = Queue()
    for u in range(1, N + 1):
        if indegree[u] == 0:
            queue.put(u)
    result = []
    while not queue.empty():
        u = queue.get()
        result.append(u)
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.put(v)
    return result


def hierarchy():
    N, K = map(int, input().split())
    graph = [[] for i in range(N + 1)]
    for u in range(1, K + 1):
        graph[u] = list(map(int, input().split()))[1:]
    result = topoSort(N, graph)
    print(result)
    boss = dict()
    boss[result[0]] = 0
    for i in range(1, len(result)):
        boss[result[i]] = result[i - 1]
    for i in range(1, N + 1):
        print(boss[i])
    return


hierarchy()

"""
King's Path

chess: 10**9 by 10**9
n segments: rith, aith, bith

Obj: minimum number of moves to get from x0,y0 to x1,y1 provided
allowed cells can be taken.

A chess king can move to any of the neighobring cells in one move

input:
x0,y0,x1,y1
n: # of segments of allowed cells
each n: description of these segments

output:
if no path between initial and final position along allowed cells -> -1
single integer -> minimum # of moves from initial to final position

example:
5 7 6 11
3
5 3 8
6 7 11
5 2 5

4
"""

from heap import heappop, heappush

dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]


def is_valid_cell(cell, mySet):
    if cell in mySet:
        return True
    return False


def get_valid_neighbor(cell, mySet):
    neighbors = []
    sr, sc = cell
    for i in range(8):
        r = sr + dr
        c = sc + dc
        neighbor = (r, c)
        # check if neighbor is valid
        if is_valid_cell(neighbor, mySet):
            neighbors.append(neighbor)


def dijkstra(start, end, mySet):
    queue = [(0, start)]
    visited = set()
    while queue:
        distance, current = heappop(queue)
        if current == end:
            return distance


def kingsPath():
    x0, y0, x1, y1 = map(int, input().split())
    n = int(input())

    pass


kingsPath()
