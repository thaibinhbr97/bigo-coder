# Dijkstra has O(V^2) for time
# However, heap can be used to bring down the time complexity to O(ElogV) or binary search tree can be used for O(ElogV)

# Source code for Dijkstra
# import queue

# MAX = 100
# INF = int(1e9)


# class Node:
#     def __initt__(self, id, dist):
#         self.id = id
#         self.dist = dist

#     def __lt__(self, other):
#         return self.dist <= other.dist


# def Dijkstra(s):
#     pq = queue.PriorityQueue()
#     pq.put(Node(s, 0))
#     dist[s] = 0
#     while pq.empty() == False:
#         top = pq.get()
#         u = top.id
#         w = top.dist
#         if dist[u] != w:
#             continue
#         for neighbor in graph[u]:
#             if w + neighbor.dist < dist[neighbor.id]:
#                 dist[neighbor.id] = w + neighbor.dist
#                 pq.put(Node(neighbor.id, dist[neighbor.id]))
#                 path[neighbor.id] = u


# if __name__ == "__main__":
#     n = int(input())
#     s, t = 0, 4
#     graph = [[] for i in range(n + 5)]
#     dist = [INF for i in range(n + 5)]
#     path = [-1 for i in range(n + 5)]
#     for i in range(n):
#         d = list(map(int, input().split()))
#         for j in range(n):
#             if d[j] > 0:
#                 graph[i].append(Node(j, d[j]))
#     Dijkstra(s)
#     ans = dist[t]
#     print(ans)

"""
Travelling cost

0,1,2,...,500 points
A-B W: A to B with a cost of W
Question: U (start) to Q other points

input:
N: # of roads
next N: A-B W <=> B-A W
U: starting point
Q: # of queries
next Q: destination V which is a min cost from U needs to be found

output:
ans on each line for each query
in case U cannot go to V -> NO PATH

example
7
0 1 4
0 3 8
1 4 1
1 2 2
4 2 3
2 5 3
3 4 2
0
4
1
4
5
7

7 -> N
0 1 4 -> A B W,...
0 3 8
1 4 1
1 2 2
4 2 3
2 5 3
3 4 2
0 -> U
4 -> Q
1 -> V,...
4
5
7
"""
# import queue

# # Constants
# MAX = 505
# INF = int(1e9)


# class Node:
#     def __init__(self, id, cost):
#         self.id = id
#         self.cost = cost

#     def __lt__(self, other):
#         return self.cost <= other.cost


# def Dijkstra(s):
#     pq = queue.PriorityQueue()
#     pq.put(Node(s, 0))
#     dist[s] = 0
#     while pq.empty() == False:
#         top = pq.get()
#         u = top.id
#         w = top.cost
#         if dist[u] != w:
#             continue
#         for neighbor in graph[u]:
#             if w + neighbor.cost < dist[neighbor.id]:
#                 dist[neighbor.id] = w + neighbor.cost
#                 pq.put(Node(neighbor.id, dist[neighbor.id]))
#                 path[neighbor.id] = u


# # Read data & define supporting variables for Dijkstra algo
# N = int(input())
# graph = [[] for i in range(MAX)]
# dist = [INF for i in range(MAX)]
# path = [-1 for i in range(MAX)]
# for i in range(N):
#     A, B, W = map(int, input().split())
#     graph[A].append(Node(B, W))
#     graph[B].append(Node(A, W))
# U = int(input())
# Q = int(input())
# Dijkstra(U)
# for i in range(Q):
#     V = int(input())
#     if dist[V] != INF:
#         print(dist[V])
#     else:
#         print("NO PATH")


"""
Mize and Maze

input:
N: # of grids
E: # of exits
T: time
M: # of connections
next M: a b w

output:
# of mices sucessfully exit within allowed time

example:
4
2
1
8
1 2 1
1 3 1
2 1 1
2 4 1
3 1 1
3 4 1
4 2 1
4 3 1
"""
# import queue

# MAX = 101
# INF = int(1e9)


# class Node:
#     def __init__(self, id, cost):
#         self.id = id
#         self.cost = cost

#     def __lt__(self, other):
#         return self.cost <= other.cost


# def Dijkstra(s):
#     pq = queue.PriorityQueue()
#     pq.put(Node(s, 0))
#     dist[s] = 0
#     while pq.empty() == False:
#         top = pq.get()
#         u = top.id
#         w = top.cost
#         for neighbor in graph[u]:
#             if w + neighbor.cost < dist[neighbor.id]:
#                 dist[neighbor.id] = w + neighbor.cost
#                 pq.put(Node(neighbor.id, dist[neighbor.id]))
#                 path[neighbor.id] = u


# # Way 1
# # since we use Dijkstra algo for each vertice, tc for this is V*ElogV with V # of nodes and E # of edges
# # N = int(input())
# # E = int(input())
# # T = int(input())
# # M = int(input())
# # graph = [[] for i in range(MAX)]
# # for i in range(M):
# #     a, b, w = map(int, input().split())
# #     graph[a].append(Node(b, w))
# # ans = 0
# # for i in range(1, N + 1):
# #     dist = [INF for i in range(MAX)]
# #     path = [-1 for i in range(MAX)]
# #     Dijkstra(i)
# #     if dist[E] <= T:
# #         ans += 1
# # print(ans)

# # Way 2
# # use Dijkstra only once, tc for this is ElogV with V # of nodes and E # of edges
# # approach: we reverse the connections between nodes starting at the exit. By doing this, we can find the minimum distance from the exit to other nodes by running
# # Dijkstra only once
# N = int(input())
# E = int(input())
# T = int(input())
# M = int(input())
# graph = [[] for i in range(MAX)]
# dist = [INF for i in range(MAX)]
# path = [-1 for i in range(MAX)]
# for i in range(M):
#     a, b, w = map(int, input().split())
#     graph[b].append(Node(a, w))
# Dijkstra(E)
# ans = 0
# for i in range(1, N + 1):
#     if dist[i] <= T:
#         ans += 1
# print(ans)

"""
The Shortest Path

input:
s <= 10: # of tests
n <= 10000: # of cities
NAME: name of city
p: # of neghbors of NAME
nr cost: NAME connections & Cost
r <= 100: # of roads
NAME1 NAME2: start end
space between different tests

output:
cost from NAME1 to NAME2
"""
import queue

INF = 200000
MAX = 10001


class Node:
    def __init__(self, id, cost):
        self.id = id
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost


def Dijkstra(s):
    pq = queue.PriorityQueue()
    pq.put(Node(s, 0))
    dist[s] = 0
    while pq.empty() == False:
        top = pq.get()
        u = top.id
        w = top.cost
        if dist[u] != w:
            continue
        for neighbor in graph[u]:
            if w + neighbor.cost < dist[neighbor.id]:
                dist[neighbor.id] = w + neighbor.cost
                pq.put(Node(neighbor.id, dist[neighbor.id]))
                path[neighbor.id] = u


# O(s*p*ElogV) - s: # of tests, p: # of queries, E: # of edges, V: # of nodes/vertices
T = int(input())  # tests
for _ in range(T):
    N = int(input())  # cities
    graph = [[] for i in range(MAX)]
    cities = {}
    for i in range(1, N + 1):
        city = input()
        cities[city] = i
        p = int(input())
        for j in range(p):
            b, w = map(int, input().split())  # connecting city with cost
            graph[i].append(Node(b, w))

    queries = int(input())
    for i in range(queries):
        dist = [INF for i in range(MAX)]
        path = [-1 for i in range(MAX)]
        start, end = map(str, input().split())
        Dijkstra(cities[start])
        print(dist[cities[end]])
    input()
